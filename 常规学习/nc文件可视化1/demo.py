import os
import datetime
import numpy as np
from netCDF4 import Dataset
import pandas as pd
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import mpl_toolkits.basemap as bm
from multiprocessing import Pool

# 解决保存图像是负号'-'显示为方块的问题
mpl.rcParams['axes.unicode_minus'] = False


# 检查文件夹是否存在,如果不存在则创建
def CheckDir(path):
    if not os.path.exists(path):
        os.mkdir(path)


# 设置地图
def DrawBasemap(xticksize=15, yticksize=15, resolution='c'):
    """
    Draw a basemap on Qinghai-Tibet Plateau and nearby area with a border a border of Plateau
    DrawBasemap(fontsize=16)
    """
    mp = bm.Basemap(llcrnrlon=60., llcrnrlat=-10., urcrnrlon=150., urcrnrlat=60., resolution=resolution,
                    projection='cyl')
    # mp.drawparallels(np.arange(-10, 60, 10), labels=[True, False, False, False], linewidth=0.5, dashes=[1, 5], fontsize=yticksize)
    # mp.drawmeridians(np.arange(70, 150, 10), labels=[False, False, False, True], linewidth=0.5, dashes=[1, 5], fontsize=xticksize)
    mp.readshapefile('/data/map_or_other/map/map-china/sheng', 'county', linewidth=0.8, color='k')


# 颜色层级
def leves_colors(var, num=1000):
    if var == 'dbz':  # dbz的层级和颜色
        levels = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        colors = ['white', 'cyan', 'lawngreen', 'limegreen', 'yellow', 'goldenrod', 'darkorange', 'red', 'firebrick',
                  'brown', 'hotpink', 'darkviolet', 'violet']
    elif var == 'rain':  # rain的层级和颜色
        levels = [0.1, 2, 4, 6, 8, 10, 20, 50]
        colors = ['#7FFFFF', '#23B6FF', '#0052CA', '#0110DB', '#9302F9', '#6D00B6', '#4D0082']
    elif var == 'temp':  # temp的层级和颜色
        if 700 <= num <= 1000:  # 700hPa-1000hPa
            levels = [-40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
            colors = ['#333333', '#595959', '#7f7f7f', '#a5a5a5', '#cccccc', '#eddaff', '#cc91ff', '#b248ff', '#9900ff',
                      '#6600ff', '#002eff', '#0a57ff', '#1481ff', '#1c96f5', '#23aceb', '#12c7e9', '#00e2e6', '#2ae273',
                      '#54e200', '#7ff000', '#aaff00', '#d4ff00', '#ffff00', '#ffe500', '#ffcc00', '#ffb200', '#ff9900',
                      '#ff6e00', '#ff4300', '#ff537f', '#ff63ff', '#ff81f3', '#ff9ee8', '#ffcef3']
        elif num == 500:  # 500hPa
            levels = [-70, -65, -60 - 55, -50, -45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10]
            colors = ['#333333', '#595959', '#7f7f7f', '#a5a5a5', '#cccccc', '#eddaff', '#cc91ff', '#b248ff', '#9900ff',
                      '#6600ff', '#002eff', '#0a57ff', '#1481ff', '#1c96f5', '#23aceb', '#12c7e9', '#00e2e6', '#2ae273',
                      '#54e200', '#7ff000', '#aaff00', '#d4ff00', '#ffff00', '#ffe500', '#ffcc00', '#ffb200', '#ff9900',
                      '#ff6e00', '#ff4300', '#ff537f', '#ff63ff', '#ff81f3', '#ff9ee8', '#ffcef3']
    elif var == 'rh':  # 850mb相对湿度
        levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
        colors = ['#ff9ee8', '#ff63ff', '#ff4300', '#ff9900', '#ffcc00', '#ffff00', '#aaff00', '#54e200', '#00e2e6',
                  '#23aceb', '#002eff', '#7f7f7f']
    elif var == 'wind':  # 风速
        levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
        colors = ['#ff9ee8', '#ff63ff', '#ff4300', '#ff9900', '#ffcc00', '#ffff00', '#aaff00', '#54e200', '#00e2e6',
                  '#23aceb', '#002eff', '#7f7f7f']
    return levels, colors


# 添加并绘制中文地名
def add_zh_sta_name(infile, zh_name, lat_name, lon_name):
    names_df = pd.read_csv(infile)  # 中文地名CSV文件
    names_temp = names_df[zh_name]  # 中文地名
    lats = names_df[lat_name]  # 地名lat
    lons = names_df[lon_name]  # 地名lon
    names = []
    for n in names_temp:  # 设置中文编码
        names.append(n.decode('utf-8'))
    for i, n in enumerate(names):
        plt.text(lons[i], lats[i], n, fontsize=13, color='b')  # 中文地名
    plt.scatter(plons, plats, s=20, color='b')  # 地名标记点


# 填色图
def Drawcontourf(lat, lon, var, levels, color):
    ctrf = plt.contourf(lon, lat, var, levels=levels, colors=color, extend='max')
    cbar = plt.colorbar(ctrf, fraction=0.03, pad=0.04)  # 填色图图例
    cbar.set_ticks(levels)


# 等值线图
def Drawcontour(lat, lon, var, nlevel, color='k', linewidth=1., fmat='%4.1f'):
    cx1 = plt.contour(lon, lat, var, nlevel, colors=color, linewidths=linewidth)
    plt.clabel(cx1, fmt=fmat)  # 等值线数值


# 风场图(风向杆)
def Drawbarbs(lat, lon, u, v, ndeltx, color='k', linewidth=1.):
    pltlat = lat[::ndeltx]
    pltlon = lon[::ndeltx]
    pltu = u[::ndeltx, ::ndeltx]
    pltv = v[::ndeltx, ::ndeltx]
    qv = plt.barbs(pltlon, pltlat, pltu, pltv, length=5, barbcolor=color, flagcolor=color, linewidth=linewidth)


# 绘图
def Drawpng(outpng, pngtext1, pngtext2, text_latlong1=(60, 62), text_latlong2=(130, 62), drawmap=True, drawconf=False, drawcon=False, drawbars=False, drawzhname=False):
    w = 10  # 设置画布宽度
    h = 10  # 设置画布高度
    dpi = 100  # 设置dpi
    fig = plt.figure(figsize=(w, h), dpi=dpi)

    if drawmap:
        DrawBasemap()  # 绘制地图

    if drawconf:
        lat = drawconf[0]
        lon = drawconf[1]
        var = drawconf[2]
        levels = drawconf[3]
        color = drawconf[4]
        Drawcontourf(lat, lon, var, levels, color)  # 绘制填色图

    if drawcon:
        lat = drawcon[0]
        lon = drawcon[1]
        var = drawcon[2]
        nlevel = drawcon[3]
        Drawcontour(lat, lon, var, nlevel, color='w', linewidth=1., fmat='%4.1f')  # 绘制等值线图

    if drawbars:
        lat = drawbars[0]
        lon = drawbars[1]
        u = drawbars[2]
        v = drawbars[3]
        ndeltx = drawbars[4]
        Drawbarbs(lat, lon, u, v, ndeltx, color='k', linewidth=1.)  # 绘制风场图(风向杆)

    if drawzhname:
        zhfile = drawzhname[0]
        zh_name = drawzhname[1]
        lat_name = drawzhname[2]
        lon_name = drawzhname[3]
        add_zh_sta_name(zhfile, zh_name, lat_name, lon_name)  # 绘制中文地名

    # 绘制标题
    plt.text(text_latlong1[0], text_latlong1[1], pngtext1.decode('utf-8'), fontsize=14, color='b')
    plt.text(text_latlong2[0], text_latlong2[1], pngtext2.decode('utf-8'), fontsize=14, color='b')

    # 保存图片
    plt.savefig(outpng, bbox_inches='tight')
    plt.close()
    print ('完成绘制：' + outpng)


def run_main(in_dir, infile, out_dir, initial_time):
    indir = in_dir + '/' + initial_time
    fcst_time = infile[4:14]  # 预报时间
    initial_time_1 = datetime.datetime.strptime(initial_time, "%Y%m%d%H")
    fcst_time_1 = datetime.datetime.strptime(fcst_time, "%Y%m%d%H")
    ntime = int((fcst_time_1 - initial_time_1).total_seconds() / 3600)  # 时间差（预报-起报）；小时

    # 读取nc数据
    file_data = Dataset(indir + '/' + infile, 'r')
    lat = file_data.variables['lat'][:]
    lon = file_data.variables['lon'][:]
    lev = file_data.variables['lev'][:]
    gh = file_data.variables['GH'][:, :, :]  # 高度
    rh = file_data.variables['R'][:, :, :]  # 相对湿度
    temp = file_data.variables['T'][:, :, :] - 273.15  # 温度
    wind_w = file_data.variables['W'][:, :, :]  # 风速 w
    wind_u = file_data.variables['U'][:, :, :]  # 风速 u
    wind_v = file_data.variables['V'][:, :, :]  # 风速 v

    lat_2 = file_data.variables['lat_2'][:]
    lon_2 = file_data.variables['lon_2'][:]
    snowd = file_data.variables['SD'][:]  # 雪深

    for nlev in lev:
        if nlev in [850]:
            # 输出格式
            out_dir_fina = out_dir + 'out' + initial_time[0:8]
            CheckDir(out_dir_fina)  # 检查输出文件夹是否存在
            # 相对湿度
            outpng = out_dir_fina + '/rh_' + str(int(nlev)) + '.t' + initial_time[8:10] + 'z.f' + str('%02i' % ntime) + '.png'  # 输出的图片名
            pngtext1 = initial_time[0:4] + '/' + initial_time[4:6] + '/' + initial_time[6:8] + '(' + initial_time[ 8:10] + ':00)起报  ' + str('%02i' % ntime) + 'h预报'
            pngtext2 = str(int(nlev)) + 'hPa 相对湿度(%)'
            var_index = np.argwhere(lev == nlev)
            levels, colors = leves_colors(var='rh')
            Drawpng(outpng, pngtext1, pngtext2, drawconf=(lat, lon, rh[int(var_index), :, :], levels, colors))

        if nlev in [925, 850, 700, 500]:
            # 输出格式
            out_dir_fina = out_dir + '/hrrr.' + initial_time[0:8]
            CheckDir(out_dir_fina)  # 检查输出文件夹是否存在
            # 位势高度/温度/风
            outpng = out_dir_fina + '/temp_' + str(int(nlev)) + '.t' + initial_time[8:10] + 'z.f' + str(
                '%02i' % ntime) + '.png'  # 输出的图片名
            pngtext1 = initial_time[0:4] + '/' + initial_time[4:6] + '/' + initial_time[6:8] + '(' + initial_time[8:10] + ':00)起报  ' + str('%02i' % ntime) + 'h预报'
            pngtext2 = str(int(nlev)) + 'hPa 位势高度(m)/温度(C)/风(m/s)'
            var_index = np.argwhere(lev == nlev)
            if nlev == 500:
                levels, colors = leves_colors(var='temp')
            else:
                levels, colors = leves_colors(var='temp')
            Drawpng(outpng, pngtext1, pngtext2,
                    drawconf=(lat, lon, temp[int(var_index), :, :], levels, colors),
                    drawcon=(lat, lon, gh[int(var_index), :, :], 80),
                    drawbars=(lat, lon, wind_u[int(var_index), :, :], wind_v[int(var_index), :, :], 10))

        if nlev in [250]:
            # 输出格式
            out_dir_fina = out_dir + '/hrrr.' + initial_time[0:8]
            CheckDir(out_dir_fina)  # 检查输出文件夹是否存在
            # 位势高度/风
            outpng = out_dir_fina + '/wind_' + str(int(nlev)) + '.t' + initial_time[8:10] + 'z.f' + str('%02i' % ntime) + '.png'  # 输出的图片名
            pngtext1 = initial_time[0:4] + '/' + initial_time[4:6] + '/' + initial_time[6:8] + '(' + initial_time[8:10] + ':00)起报  ' + str('%02i' % ntime) + 'h预报'
            pngtext2 = str(int(nlev)) + 'hPa 位势高度(m)/温度(C)/风(m/s)'
            var_index = np.argwhere(lev == nlev)
            levels, colors = leves_colors(var='wind')
            wind = np.sqrt((wind_u[int(var_index), :, :] ** 2) + (wind_v[int(var_index), :, :] ** 2))
            Drawpng(outpng, pngtext1, pngtext2, drawconf=(lat, lon, wind[:, :], levels, colors), drawcon=(lat, lon, gh[int(var_index), :, :], 80), drawbars=(lat, lon, wind_u[int(var_index), :, :], wind_v[int(var_index), :, :], 10))

    # 输出格式
    out_dir_fina = out_dir + '/hrrr.' + initial_time[0:8]
    CheckDir(out_dir_fina)  # 检查输出文件夹是否存在
    # 位势高度/温度/风
    outpng = out_dir_fina + '/rh_500' + '.t' + initial_time[8:10] + 'z.f' + str('%02i' % ntime) + '.png'  # 输出的图片名
    pngtext1 = initial_time[0:4] + '/' + initial_time[4:6] + '/' + initial_time[6:8] + '(' + initial_time[8:10] + ':00)起报  ' + str('%02i' % ntime) + 'h预报'
    pngtext2 = '850-500hPa 平均相对湿度(%)/700hPa 风(m/s)'
    levels, colors = leves_colors(var='rh')
    rh_avg = (rh[4, :, :] + rh[5, :, :] + rh[6, :, :] + rh[7, :, :] + rh[8, :, :]) / 5.
    Drawpng(outpng, pngtext1, pngtext2, drawconf=(lat, lon, rh_avg[:, :], levels, colors),
            drawbars=(lat, lon, wind_u[6, :, :], wind_v[6, :, :], 10))

# 输入输出路径
initial_time = '20210218123000'
in_dir = 'data'
out_dir ='pic'
infiles = os.listdir(in_dir + '/' + initial_time)
for infile in infiles:
    run_main(in_dir, infile, out_dir, initial_time)
