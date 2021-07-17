import rasterio
import rasterio.features
import rasterio.warp
import xml.etree.ElementTree as ET

class Converter:
    def __init__(self):
        pass
    
    # Conversion of .tif to GeoJSON format
    def tif_to_geojson(self, TIFFILENAME):
        geo_json_list = []
        with rasterio.open(TIFFILENAME) as dataset:
            # Read the dataset's valid data mask as ndarray.
            mask = dataset.dataset_mask()
            # Extract feature shapes and values from the array.
            for geom, val in rasterio.features.shapes(
                    mask, transform=dataset.transform):
                    # Transform shapes from the dataset's own coordinate
                    # reference system to CRS84 (EPSG:4326).
                    geom = rasterio.warp.transform_geom(
                        dataset.crs, "EPSG:4326", geom, precision=6)
                    # add GeoJSON shapes to list
                    geo_json_list.append(geom)
        # The last element creates an inverted shapefile so should be removed for clarity
        return geo_json_list[:-1]
    
    # Parse xml to enrich feature
    # Useful for builting FeatureCollection GeoJSON set
    def feature_enrich(self, XMLFILENAME):
        tree = etree.parse(XMLFILENAME)
        features = {}
        features["realm"] = [i.text for i in tree.findall('.//Realm')]
        features["biome"] = [i.text for i in tree.findall('.//Biome')]
        features["name"] = [i.text for i in tree.findall('.//Name')]
        return features
    
    # Construct a GeometryCollection type GeoJSON
    def GeometryCollection(self, TIFFILENAME):
        geo = {"type": "GeometryCollection"}
        geo["geometries"] = self.tif_to_geojson(TIFFILENAME)
        return geo