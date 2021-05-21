from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from osgeo import gdal_array

# 读取dem文件
path = r"F:\内蒙古项目\呼市\hebing.tif"
# 将dem文件转为np.array数组
lmsdem = gdal_array.LoadFile(path)
nrows, ncols = lmsdem.shape

# 设置x轴坐标
x_array = np.zeros((nrows,ncols))
def xaxis(a,b):
  for i in range(a,b):
      x_array[i,:] = i
  return x_array
x = xaxis(0,nrows)

# 设置y轴坐标
y_array = np.zeros((nrows,ncols))
def yaxis(a,b):
  for i in range(a,b):
      y_array[:,i] = i
  return y_array
y = yaxis(0,ncols)


# 设置绘制区域的范围
region = np.s_[1300:1500,1150:1400]
x,y,z = x[region],y[region],lmsdem[region]
fig = plt.figure()
ax = Axes3D(fig)


ls = LightSource(270, 45)
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
