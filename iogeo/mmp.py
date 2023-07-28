"""
Interface for NumPy's memory-mapped files.

np.memmap provides allows you to work with large datasets that 
do not fit entirely into memory. It maps a file on disk 
to an array in memory, enabling you to read and write data 
in small portions without loading the entire dataset into RAM.
It provides a NumPy-like interface, allowing you to perform 
array operations and computations as you would with in-memory 
arrays.
No additional data storage: When using np.memmap, you do not 
need to create additional copies of your data, as it directly 
reads from the file on disk. This can save storage space, 
especially when dealing with very large datasets.
Supports multiple file formats: np.memmap can work with 
different data file formats (e.g., binary, ASCII) and different 
data types, making it versatile for various data storage and 
processing needs.
"""
import os
import numpy as np
from autologging import logged, traced

@traced
@logged
def read_mmp(fname, shape, mmp_dtype=np.float32, **kwargs):
  """
  Read a memory-mapped file.

  Parameters
  ----------
  fname : str
    The file name, including the '.mmp' extension.

  shape : tuple
    Shape of the array stored in the memory-mapped file.

  mmp_dtype : data-type, optional (default is np.float32)
    The data type to interpret the binary data in the file.

  Returns
  -------
  np.memmap
    The memory-mapped array.

  Raises
  ------
  FileNotFoundError
    If the specified file does not exist.

  """
  if not os.path.exists(fname):
    raise FileNotFoundError(fname)
  
  fA = np.memmap(fname, dtype=mmp_dtype, shape=shape)
  return fA

@traced
@logged
def save_mmp(A, fname, mmp_dtype=np.float32, **kwargs):
  """
  Save an array to a memory-mapped file.
  
  Parameters
  ----------
  A : array_like
    The array to be saved to the memory-mapped file.

  fname : str
    The file name, including the '.mmp' extension.

  mmp_dtype : data-type, optional (default is np.float32)
    The data type to be used for saving the array.

  Returns
  -------
  np.memmap
    The memory-mapped array.

  """
  with open(fname, 'wb') as file:
    A.tofile(file)

  fA = np.memmap(fname, dtype=mmp_dtype, mode='r+', shape=A.shape)
  return fA
