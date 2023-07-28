import numpy as np
import os
import sys
import unittest
from ..mmp import read_mmp, save_mmp

class TestMMPFunctions(unittest.TestCase):

  def setUp(self):
    self.test_fname = "test_mmp_file.mmp"
    self.shape = (3, 3)
    self.data = np.random.rand(*self.shape).astype(np.float32)

  def tearDown(self):
    if os.path.exists(self.test_fname):
      os.remove(self.test_fname)

  def test_read_mmp(self):
    # Save test data to the memory-mapped file
    save_mmp(self.data, self.test_fname)

    # Read the data back from the memory-mapped file
    read_data = read_mmp(self.test_fname, self.shape)

    # Check if the data read from the file matches the original data
    np.testing.assert_array_equal(read_data, self.data)

  def test_save_mmp(self):
    # Save the test data to the memory-mapped file
    save_mmp(self.data, self.test_fname)

    # Read the data back from the memory-mapped file
    read_data = read_mmp(self.test_fname, self.shape)

    # Check if the data read from the file matches the original data
    np.testing.assert_array_equal(read_data, self.data)

  def test_read_and_save_3d_array(self):
    # Create a sample 3D array
    shape = (3, 4, 5)
    dtype = np.float32
    sample_array = np.random.rand(*shape).astype(dtype)

    # Save the array to a memory-mapped file
    test_fname = "test_array.mmp"
    save_mmp(sample_array, test_fname)

    # Read the memory-mapped array and compare with the original array
    read_array = read_mmp(test_fname, shape)
    np.testing.assert_array_equal(sample_array, read_array)

    # Clean up: remove the test file
    os.remove(test_fname)

if __name__ == '__main__':
  unittest.main()
