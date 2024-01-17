from autologging import logged, traced
import geopandas as gpd
from rioxarray import open_rasterio

@traced
@logged
def read_shp(file_path, **kwargs):
  return gpd.read_file(file_path, **kwargs)

@traced
@logged
def read_tif(file_path, **kwargs):
  return open_rasterio(file_path, **kwargs)
