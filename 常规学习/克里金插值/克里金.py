import math
import numpy as np
import pandas as pd
import geopandas as gpd
import xarray as xr
import salem
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.io.shapereader import Reader, natural_earth
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pykrige.ok import OrdinaryKriging
import os
import matplotlib as mpl
import matplotlib.colors as col
import matplotlib.cm as cm


def create_map(fig):
    shp_path = r'China_shp_lqy/'
    # --创建画图空间
    proj = ccrs.LambertConformal(central_longitude=110, central_latitude=35,
                                 standard_parallels=(30, 60))  # 创建坐标系

    ax = fig.subplots(1, 1, subplot_kw={'projection': proj})
    # --设置shp
    provinces = cfeat.ShapelyFeature(
        Reader(shp_path + 'province.shp').geometries(),
        ccrs.PlateCarree(),
        edgecolor='k',
        facecolor='none',
    )
    ax.add_feature(provinces, linewidth=0.6, zorder=2)
    # --设置范围
    ax.set_extent([80, 135, 15, 55], crs=ccrs.PlateCarree())
    # --关闭边框
    ax.spines['geo'].set_visible(False)
    # --设置刻度
    ax.tick_params(
        axis='both',
        labelsize=5,
        direction='out',
        labelbottom=False,
        labeltop=False,
        labelleft=False,
        labelright=False
    )
    # --设置小地图
    left, bottom, width, height = 0.675, 0.13, 0.23, 0.27
    ax2 = fig.add_axes(
        [left, bottom, width, height],
        projection=ccrs.PlateCarree()
    )
    provinces = cfeat.ShapelyFeature(
        Reader(shp_path + 'province.shp').geometries(),
        ccrs.PlateCarree(),
        edgecolor='k',
        facecolor='gray',
    )
    ax2.add_feature(provinces, linewidth=0.6, zorder=2)
    ax2.set_extent([105, 125, 0, 25], crs=ccrs.PlateCarree())
    return ax


def krige_interp(df):
    # 插值成0.25*0.25
    grid_lon = np.arange(float(math.floor(df.lon.min())), float(math.ceil(df.lon.max())), 0.25)
    grid_lat = np.arange(float(math.floor(df.lat.min())), float(math.ceil(df.lat.max())), 0.25)
    lons = df["lon"].values
    lats = df["lat"].values
    data = df["data"].values

    # 调用克里金插值函数
    OK = OrdinaryKriging(lons, lats, data,
                         variogram_model='gaussian',
                         coordinates_type="geographic",
                         nlags=6, )
    z, ss = OK.execute('grid', grid_lon, grid_lat)
    # 转换成网格
    xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)
    # 将插值网格数据整理
    df_grid = pd.DataFrame(dict(lon=xgrid.flatten(), lat=ygrid.flatten()))
    # 添加插值结果
    df_grid['data'] = z.flatten()
    df_grid = df_grid.set_index(['lat', 'lon'])
    ds = xr.Dataset.from_dataframe(df_grid).data
    return ds


def mask_region(ds, region='china'):
    shp_path = r'China_shp_lqy/'
    shp = gpd.read_file(shp_path + 'province.shp').set_index('省')
    if region != 'china':
        shp = shp.loc[region, :]
    ds_mask = ds.salem.roi(shape=shp)
    return ds_mask


def draw_fig(ds, levels, outpath='.'):
    fig = plt.figure(figsize=(10, 7), dpi=130)  # 创建页面

    # 自定义cmap颜色
    color1 = '#00E400'  # 优
    color2 = '#FFFF00'  # 良
    color3 = '#FF7E00'  # 轻
    color4 = '#FF0000'  # 中
    color5 = '#99004C'  # 重
    color6 = '#7E0023'  # 严重
    cmap2 = col.LinearSegmentedColormap.from_list('own2', [color1, color2, color3,color4, color5, color6])
    cm.register_cmap(cmap=cmap2)


    im = ds.plot.contourf(
        ax=create_map(fig),
        cmap=cm.get_cmap('own2'),
        transform=ccrs.PlateCarree(),
        levels=levels,
        add_colorbar=False,
    )
    cbar_ax = fig.add_axes([0.13, 0.17, 0.3, 0.012])
    cb = fig.colorbar(im, cax=cbar_ax, orientation='horizontal')
    plt.savefig(f'{outpath}{os.sep}kriging_mask_chinamap.png')


if __name__ == "__main__":
    data_file = r'data.csv'
    levels = np.array([0,35,75,115,150,250,350])
    print(type(levels))
    df = pd.read_csv(data_file, header=0, names=['lon', 'lat', 'data'])
    ds = krige_interp(df)
    ds_mask = mask_region(ds)
    draw_fig(ds_mask, levels)