# Computer readible ecological data

## Requirements
* python3
  * [rasterio](https://rasterio.readthedocs.io/en/latest/installation.html)

* disk space of 3G for the raw data + geojson output

## Quickstart

1. Download all shapefiles using [zdl](https://github.com/10ego/zenodo_downloader) under `/scripts`
2. Unpack all data (`ls *.bz2 | xargs -n1 tar --one-top-level -xvjf`)
3. Run python script (`python processor.py`)
