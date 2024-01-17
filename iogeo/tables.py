from autologging import logged, traced
import json
import pandas as pd


@traced
def read_csv(file_path, header=0, **kwargs):
  return pd.read_csv(file_path, header=header, **kwargs)
@traced
def read_json(file_path, **kwargs):
  with open(file_path, 'r') as file:
    content = json.load(file, **kwargs)
  return content
@traced
def save_json(file_path, di: dict, **kwargs):
  with open(file_path, 'w') as file:
    json.dump(di, file, **kwargs)
@traced
def read_xlsx(file_path, header=1, **kwargs):
  return pd.read_excel(file_path, header=header, **kwargs)