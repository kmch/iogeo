import os
import numpy as np
from autologging import logged, traced

mmp_dtype=np.float32

@traced
@logged
def read_mmp(fname, shape, mmp_dtype=np.float32, **kwargs):
  """
  Read a memory-mapped file.

  fname : str 
    Including .mmp extension.  
  shape : tuple
    Shape of the array stored in fname.
    (this is necessary).
    
  Notes
  -----
  See top lines of this module:
  mmp_dtype = np.float32 
  
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
  
  fname : str 
    Including .mmp extension.
    
  Notes
  -----
  See top lines of this module:
  mmp_dtype = np.float32 
  
  """
  with open(fname, 'wb') as file:
    A.tofile(file)

  fA = np.memmap(fname, dtype=mmp_dtype, mode='r+', shape=A.shape)
  return fA