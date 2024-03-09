#!/bin/bash
#
# Copyright (C) 2023 OpenSearch Geonames.
#
# OpenSearch Geonames is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

# mappings from: https://github.com/openeventdata/es-geonames
curl -XPUT 'localhost:9200/geonames' -H 'Content-Type: application/json' -d @geonames.json
