#
# Copyright (C) 2023 Geonames Indexer.
#
# Geonames Indexer is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames Indexer module."""

from .index import index_geonames

__version__ = "0.1.0"

__all__ = ("__version__", "index_geonames")
