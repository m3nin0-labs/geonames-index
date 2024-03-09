#
# Copyright (C) 2023 Geonames Indexer.
#
# Geonames Indexer is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames Indexer configuration module."""

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="GEONAMES",
    settings_files=["settings.toml"],
)
