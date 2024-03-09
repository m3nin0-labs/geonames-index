#
# Copyright (C) 2023 Geonames Indexer.
#
# Geonames Indexer is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames Indexer Reader module."""

import csv
from datetime import datetime
from pathlib import Path
from typing import Generator, List, Union

import pycountry


def _convert_iso_alpha2_to_alpha3(alpha_2_code: str) -> str:
    """Convert ISO 3166-1 Alpha 2 into Alpha 3.

    Args:
        alpha_2_code (str): ISO 3166-1 Alpha 2 code.

    Returns:
        str: ISO 3166-1 Alpha 3 code.
    """
    return pycountry.countries.get(alpha_2=alpha_2_code).alpha_3


def check_file_exists(file: Union[Path, List[Path]]):
    """Check if a file exists."""

    def _check_file(file):
        if not file.exists():
            raise FileNotFoundError(f"{file.as_posix()} doesn't exists.")

    if isinstance(file, list):
        for file in file:
            _check_file(file)

    else:
        _check_file(file)


def read_geonames_adm_file(file: Path) -> dict:
    """Read Geonames Adm (1 or 2) file.

    Args:
        file (Path): Adm file (1 or 2).

    Returns:
        dict: Adm file content as dict.
    """
    # reading the file
    file_content = {}

    with file.open("rt", encoding="utf-8") as ifile:
        reader = csv.reader(ifile, delimiter="\t")

        for row in reader:
            file_content[row[0]] = row[1]

    return file_content


def read_geonames_data_file(
    index: str, file: Path, adm1_data: dict, adm2_data: dict
) -> Generator[dict, None, None]:
    """Read Geonames data file.

    Args:
        index (str): Geonames index.

        file (Path): Geonames data file (extracted from ``allCountries.zip``).

        adm1_data (dict): ADM1 data as dict.

        adm2_data (dict): ADM2 data as dict.

    Returns:
        dict: Data file content as dict.

    Note:
        This function was adapted from ``os-geonames`` code
        (https://github.com/openeventdata/es-geonames/blob/master/geonames_elasticsearch_loader.py)
    """
    with file.open("rt", encoding="utf-8") as ifile:
        reader = csv.reader(ifile, delimiter="\t")

        for row in reader:
            processing_date = datetime.today().strftime("%Y-%m-%d")

            try:
                coords = row[4] + "," + row[5]
                country_code = _convert_iso_alpha2_to_alpha3(row[8])
                alt_names = list(set(row[3].split(",")))

                # Transformation for USA records
                if str(row[0]) == "6252001":
                    alt_names.append("US")
                    alt_names.append("U.S.")
                if str(row[0]) == "239880":
                    alt_names.append("C.A.R.")

                alt_name_length = len(alt_names)

                # get ADM1 name
                if row[10]:
                    country_admin1 = ".".join([row[8], row[10]])
                    try:
                        admin1_name = adm1_data[country_admin1]
                    except KeyError:
                        admin1_name = ""
                else:
                    admin1_name = ""

                # Get ADM2 name
                if row[11]:
                    country_admin2 = ".".join([row[8], row[10], row[11]])
                    try:
                        admin2_name = adm2_data[country_admin2]
                    except KeyError:
                        admin2_name = ""
                else:
                    admin2_name = ""

                document = {
                    "geonameid": row[0],
                    "name": row[1],
                    "asciiname": row[2],
                    "alternativenames": alt_names,
                    "coordinates": coords,  # 4, 5
                    "feature_class": row[6],
                    "feature_code": row[7],
                    "country_code3": country_code,
                    "admin1_code": row[10],
                    "admin1_name": admin1_name,
                    "admin2_code": row[11],
                    "admin2_name": admin2_name,
                    "admin3_code": row[12],
                    "admin4_code": row[13],
                    "population": row[14],
                    "alt_name_length": alt_name_length,
                    "modification_date": processing_date,
                }

                yield {
                    "_id": document["geonameid"],
                    "_source": document,
                    "_index": index,
                }

            except Exception:
                pass
