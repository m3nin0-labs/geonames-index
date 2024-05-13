# Geonames Index

The Geonames Index is designed to streamline the process of downloading, transforming, and indexing data from the comprehensive Geonames database into an Opensearch instance. This solution is ideal for anyone looking to leverage geographical data for search applications, data analysis, or geographic information systems.

> **Note**: This is a hobby project.

## Features

- (1) Automated download of Geonames data;
- (2) Data transformation scripts for preparing the data for indexing;
- (3) Integration with Opensearch for powerful search capabilities;
- (4) Simple and efficient management of operations through a Makefile.

## Getting Started

Below are the steps, based on `make`, to configure and use the Geonames Index project:

**1. Download the Geonames Files**

To download the necessary Geonames files, run:
```
make files-download
```

**2. Start Opensearch**

Launch your Opensearch instance using Docker:

```
make os-start
```

**3. Create the Geonames Index**

Set up the Geonames index with the appropriate mappings:

```
make os-mappings
```

**4. Index the Data**

Begin the data indexing process:

```
make os-index
```

To index data, make sure you have the `geonames` library installed. You can install using the following command:

```sh
pip install .
```

## Rest API

If you want to explore the Geonames data using a Rest API, check the [Geonames Search project](https://github.com/m3nin0-labs/geonames-search).

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## Acknowledge

The mappings and base transformations used on this repository, cames from [es-geonames](https://github.com/openeventdata/es-geonames). Thanks!

## License

`geonames-index` is distributed under the MIT license. See LICENSE for more details.
