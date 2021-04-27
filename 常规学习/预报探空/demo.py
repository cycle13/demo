import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import netCDF4 as nc
import os

import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo, SkewT
from metpy.units import units

# 使得中文字体不乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# os.chdir('D:/ERA5')
# deta = 4
CI_file = r'data/ECMWF_utci_20210404_v1.0_int.nc'
# no_CI_file = 'D:/ERA5/no_CI_hecheng/' + str(deta) + '_smooth_pressure.nc'

gap = 0.25

# 该范围包含多少个经纬度格点
# grid_num = int(deta / gap) * 2 + 1


def plot_skewt_with_mepy(file,
                         time_deta=0,
                         top_level=20,
                         point_x_y=[20, 20],
                         fontsize=20,
                         ):
    '''
    func: 输入.nc文件，获取里面的p t td u v
    inputs:
        file:文件绝对路径 + 文件名称，eg: D:/ERA5/CI_hecheng/4_smooth_pressure.nc
        time_deta: 默认0, 即对应14:00
        top_level: 探空图中顶层气压层，默认为20hPa
        point_x_y: 选取哪个位置画出探空， 默认[20,20]
        fontsize: 字体大小，默认20

    return:
    '''

    Vars = ['t', 'q',
            'u',
            'v',
            'Td'
            ]

    Vars_operation = ['-273.16', '*1e3',
                      '*1',
                      '*1',
                      '-273.16'
                      ]

    # 默认的以14:00为中间时间，对应的time_index = 30
    time_center = 14

    # 确定探空点所在位置
    point_x = point_x_y[0]
    point_y = point_x_y[1]

    fr = nc.Dataset(file)

    # 顶层气压在气压层中的 index, 和需要的气压

    top_level_index = list(fr['level'][::-1]).index(top_level)
    p = np.array(fr['level'][::-1][0:top_level_index + 1]) * units.hPa
    print('p.shape:', p.shape)

    all_data = []
    for Var, oper in zip(Vars, Vars_operation):
        # 确定本地时间, index=30表示北京时14时
        current_time_index = 30 + time_deta
        # local_beijing_time = time[current_time_index]+8
        local_beijing_time = time_center + time_deta
        print('local_beijing_time:', local_beijing_time)

        # 数据是从最高层开始排序的，因此，需要进行颠倒过来
        print(Var)
        Var_data = fr[Var][:][current_time_index][-1::-1, -1::-1, :]

        Var_data = np.array(Var_data)[0:top_level_index + 1, point_x, point_y]
        print(Var_data.shape)

        # 对数据进行处理
        Var_data = eval('Var_data' + oper)
        all_data.append(Var_data)

    fr.close()

    # 按照官网例子进行数据处理和类型转换
    T = all_data[Vars.index('t')] * units.degC
    Td = all_data[Vars.index('Td')] * units.degC
    u = all_data[Vars.index('u')] * units.knots
    v = all_data[Vars.index('v')] * units.knots

    # 如果不进行数据类型转换，就会报错
    #    T = all_data[Vars.index('t')]
    #    Td = all_data[Vars.index('Td')]
    #    u = all_data[Vars.index('u')]
    #    v = all_data[Vars.index('v')]

    # 创建一个子图和句柄 ax
    fig1, ax = plt.subplots(1, 1, figsize=(9, 9))
    skew = SkewT(fig1, rotation=30)

    ##画出温度，露点廓线和水平uv风场
    skew.plot(p, T, 'r')
    skew.plot(p, Td, 'g')
    skew.plot_barbs(p, u, v)

    # Calculate LCL height and plot as black dot. Because `p`'s first value is
    # ~1000 mb and its last value is ~250 mb, the `0` index is selected for
    # `p`, `T`, and `Td` to lift the parcel from the surface. If `p` was inverted,
    # i.e. start from low value, 250 mb, to a high value, 1000 mb, the `-1` index
    # should be selected.

    # 基于地面气压、温度和露点(以1000hPa充当地面)，计算出抬升凝结高度LCL,并在图上标出
    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
    skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')

    # 计算出气块绝热路径，用黑色线条表示
    # Calculate full parcel profile and add to plot as black line
    prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
    skew.plot(p, prof, 'k', linewidth=2)

    # 计算出CAPE 和 CIN面积
    # Shade areas of CAPE and CIN
    skew.shade_cin(p, T, prof)
    skew.shade_cape(p, T, prof)

    # 计算cape和cin值
    cape, cin = mpcalc.cape_cin(p, T, Td, prof,
                                which_el='most_cape',
                                )
    print('cape:', cape)
    print('cin:', cin)

    # An example of a slanted line at constant T -- in this case the 0
    # isotherm
    # 将 0 温度等值线画出来
    skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)

    # Add the relevant special lines
    # 画出干绝热线、湿绝热线和 混合比线
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()

    fontdict = {'fontsize': fontsize}
    # 设置横纵坐标数值范围
    x_left = -40
    x_right = 60
    skew.ax.set_ylim(1000, 100)
    skew.ax.set_xlim(x_left, x_right)

    # 设置对应的xtickslabel 和 ytickslabel
    # 对应的句柄是 skew.ax
    y_ticks = np.arange(1000, 0, -100)
    y_tickslabel = np.arange(1000, 0, -100)

    x_ticks = np.arange(x_left, x_right + 10, 10)
    x_tickslabel = np.arange(x_left, x_right + 10, 10)

    skew.ax.set_yticks(y_ticks)
    skew.ax.set_yticklabels(y_tickslabel, fontdict=fontdict)

    skew.ax.set_xticks(x_ticks)
    skew.ax.set_xticklabels(x_tickslabel, fontdict=fontdict)

    # 设置横纵label
    skew.ax.set_ylabel('Height/hPa', fontsize=fontsize)
    skew.ax.set_xlabel('T/(℃)', fontsize=fontsize)

    # 由于是在子图上画的skew的，因此ax的横纵坐标轴上，
    # 会自动出现一些数字，可以使用ax.set_ticklabels功能使其不显示
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    # Show the plot
    plt.show()

    # 可以查看设置了tickslabel后的ticks数值
    print('ax 的ticks：', ax.get_yticklabels()[:])


    print()
    print('skewt 的ticks：', skew.ax.get_yticklabels()[:])

plot_skewt_with_mepy(CI_file,
                     time_deta=3,
                     top_level=200,
                     point_x_y=[20, 25],
                     )

'''
outputs:
cape: 673.6904340493442 joule / kilogram
cin: -231.31875105377705 joule / kilogram

ax 的ticks： [Text(0, 0.0, ''), Text(0, 0.2, ''), Text(0, 0.4, ''), Text(0, 0.6000000000000001, ''), Text(0, 0.8, ''), Text(0, 1.0, '')]

skewt 的ticks： [Text(0, 1000, '1000'), Text(0, 900, '900'), Text(0, 800, '800'), Text(0, 700, '700'), Text(0, 600, '600'), Text(0, 500, '500'), Text(0, 400, '400'), Text(0, 300, '300'), Text(0, 200, '200'), Text(0, 100, '100')]
'''
