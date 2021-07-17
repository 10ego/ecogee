import json
import GeoShaper
import os

Converter = GeoShaper.Converter()

dirs = [d for d in os.listdir('data') if not d.endswith('bz2')]
counter = 0
for d in dirs:
    counter+=1
    ls = os.listdir(f'data/{d}')
    for f in ls:
        if f.endswith('tif'):
            TIFFILENAME = f'data/{d}/{f}'
# Not currently using xml to build a FeatureCollection
#        elif f.endswith('xml'):
#            XMLFILENAME = f
    print(f"Converting {TIFFILENAME} ({counter}/{len(dirs)})..")
    geojson = Converter.GeometryCollection(TIFFILENAME)
    with open(f'geojson/{d}.geojson','w+') as f:
        json.dump(geojson, f)