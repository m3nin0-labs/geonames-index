#
# Copyright (C) 2023 Geonames Indexer.
#
# Geonames Indexer is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames Indexer index module."""

from pathlib import Path
from typing import List, Union

from opensearchpy import OpenSearch, helpers

from . import mutator
from .config import settings


#
# Utilities
#
def create_search_client():
    """Create an OpenSearch client.

    Note:
        To configure the client, please use the ``settings.toml`` file.
    """
    return OpenSearch(**settings.opensearch.config)


#
# Indexer
#
class Indexer:
    """Indexer class."""

    _index = None
    """Index name."""

    def __init__(self, index: str) -> None:
        """Initializer.

        Args:
            index (str): Name of the index.
        """
        self._index = index
        self._client = create_search_client()

    def bulk(self, actions: List[dict]):
        """Bulkd index."""
        helpers.bulk(client=self._client, actions=actions)


#
# Utilities
#
def index_geonames(
    index: str,
    geonames_data_file: Union[str, Path],
    geonames_adm1_file: Union[str, Path],
    geonames_adm2_file: Union[str, Path],
):
    """Index Geonames data.

    Args:
        index (str): Geonames index.

        geonames_data_file (Union[str, Path]): Geonames data file.

        geonames_adm1_file (Union[str, Path]): Geonames adm1 file.

        geonames_adm2_file (Union[str, Path]): Geonames adm2 file.
    Returns:
        None
    """
    actions = mutator.mutate_geonames_into_actions(
        index, geonames_data_file, geonames_adm1_file, geonames_adm2_file
    )

    # indexing
    indexer = Indexer(index)
    indexer.bulk(actions)
