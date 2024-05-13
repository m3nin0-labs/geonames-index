#
# Copyright (C) 2023 Geonames Indexer.
#
# Geonames Indexer is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames Indexer example."""

from geonames import index_geonames

#
# General definitions
#
index_name = "geonames"

# Data from: https://www.geonames.org/export/
# To learn more: https://download.geonames.org/export/dump/readme.txt
geonames_data_file = "data/allCountries.txt"
geonames_adm1_file = "data/admin1CodesASCII.txt"
geonames_adm2_file = "data/admin2Codes.txt"

#
# 1. Indexing data
#
index_geonames(
    index=index_name,
    geonames_data_file=geonames_data_file,
    geonames_adm1_file=geonames_adm1_file,
    geonames_adm2_file=geonames_adm2_file,
)
