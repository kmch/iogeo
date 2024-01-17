from autologging import logged, traced
import os

from .mmp import read_mmp, save_mmp
from .spatial import read_shp, read_tif
from .tables import read_csv, read_json, save_json, read_xlsx

@traced
@logged
def read(file_path, **kwargs):
  _, extension = os.path.splitext(file_path)
  extension = extension[1:] # remove the dot

  if extension == 'csv':
    read_fun = read_csv

  elif extension == 'json':
    read_fun = read_json
  
  elif extension == 'mmp':
    read_fun = read_mmp

  elif extension == 'shp':
    read_fun = read_shp

  elif extension == 'tif':
    read_fun = read_tif
  
  elif extension == 'xlsx' or extension == 'xls':
    read_fun = read_xlsx
  
  else:
    raise ValueError('Unknown extension: %s' % extension)
    
  return read_fun(file_path, **kwargs)

@traced
@logged
def save(file_path, data, **kwargs):
  _, extension = os.path.splitext(file_path)
  extension = extension[1:] # remove the dot

  # if extension == 'csv':
  #   save_fun = read_csv

  if extension == 'json':
    save_fun = save_json
  
  # elif extension == 'mmp':
  #   save_fun = read_mmp

  # elif extension == 'shp':
  #   save_fun = read_shp

  # elif extension == 'tif':
  #   save_fun = read_tif
  
  # elif extension == 'xlsx' or extension == 'xls':
  #   save_fun = read_xlsx
  
  else:
    raise ValueError('Unknown extension: %s' % extension)
    
  return save_fun(file_path, data, **kwargs)



