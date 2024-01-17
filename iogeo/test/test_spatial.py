def test_read_tif():
  from rioxarray import open_rasterio
  name = 'LIDAR_Composite_10m_DTM_2022_521500_540000_152500_179500.tif'
  rds = open_rasterio('../../examples/data/%s' % name)
  