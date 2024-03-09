#
# Copyright (C) 2023 Geonames Indexer.
#
# Geonames Indexer is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames Indexer Mutations module."""

from pathlib import Path
from typing import Generator, Union

from . import reader


def mutate_geonames_into_actions(
    index: str,
    geonames_data_file: Union[str, Path],
    geonames_adm1_file: Union[str, Path],
    geonames_adm2_file: Union[str, Path],
) -> Generator[dict, None, None]:
    """Mutate Geonames files into Index actions.

    Args:
        index (str): Geonames index.

        geonames_data_file (Union[str, Path]): Geonames data file in txt format
        (extracted from ``allCountries.zip``).

        geonames_adm1_file (Union[str, Path]): Geonames adm1 file in txt format.

        geonames_adm2_file (Union[str, Path]): Geonames adm2 file in txt format.
    """
    geonames_data_file = Path(geonames_data_file)
    geonames_adm1_file = Path(geonames_adm1_file)
    geonames_adm2_file = Path(geonames_adm2_file)

    # checking if files exists
    reader.check_file_exists(
        [geonames_data_file, geonames_adm1_file, geonames_adm2_file]
    )

    # reading data
    adm1_data = reader.read_geonames_adm_file(geonames_adm1_file)
    adm2_data = reader.read_geonames_adm_file(geonames_adm2_file)

    return reader.read_geonames_data_file(
        index, geonames_data_file, adm1_data, adm2_data
    )
