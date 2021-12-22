import requests
from urllib.request import urlopen
import pandas as pd
import json
import geopandas

gdf = geopandas.read_file("https://opendata.arcgis.com/datasets/a0e3a1c53ad8422faf00604ee08955db_0.geojson")

print(gdf.head())

df1 = pd.DataFrame(gdf)

url = "https://opendata.arcgis.com/datasets/a0e3a1c53ad8422faf00604ee08955db_0.geojson"
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
print(key + ':', value)

#looking for solutions here, but failing
#https://coderedirect.com/questions/541136/read-json-to-pandas-dataframe-valueerror-mixing-dicts-with-non-series-may-lea

df = pd.json_normalize("https://opendata.arcgis.com/datasets/a0e3a1c53ad8422faf00604ee08955db_0.geojson")
