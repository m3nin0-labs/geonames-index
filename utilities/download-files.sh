#!/bin/bash
#
# Copyright (C) 2023 OpenSearch Geonames.
#
# OpenSearch Geonames is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

mkdir -p data

#
# Download countries data
#
wget https://download.geonames.org/export/dump/allCountries.zip -O data/allCountries.zip

unzip data/allCountries.zip -d data/

#
# Download adm codes
#
wget https://download.geonames.org/export/dump/admin1CodesASCII.txt -O data/admin1CodesASCII.txt
wget https://download.geonames.org/export/dump/admin2Codes.txt -O data/admin2Codes.txt
