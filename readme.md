# Ecoregion shapefile processor

Converts the ecoregion shapefiles provided under [this Zenodo record](https://zenodo.org/record/4018314) to a geojson format so it can be used with Google Earth Engine

## Requirements
* python3
  * [rasterio](https://rasterio.readthedocs.io/en/latest/installation.html)

* disk space of 3G for the raw data + geojson output

## Quickstart

1. Download all shapefiles using [zdl](https://github.com/10ego/zenodo_downloader) under `/scripts`
2. Unpack all data (`ls *.bz2 | xargs -n1 tar --one-top-level -xvjf`)
3. Run python script (`python processor.py`)

## Data dump
A complete package of converted files are available here: [Dropbox link](https://www.dropbox.com/s/0ojy6xuyfzpxc4a/geojson.tar.gz?dl=1)
