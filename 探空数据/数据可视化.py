# 读取数据
import pandas as pd
import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo,SkewT
from metpy.units import units
import matplotlib.pyplot as plt
df = pd.read_excel('data/tankong.xlsx',sheet_name=None)



for k in df.keys():
    try:
        df = pd.read_excel('data/tankong.xlsx',sheet_name=k)
        # 数据可视化
        p = df['pressure'].values * units.hPa
        T = df['TMP'].values * units.degC
        Td = df['dewpoint'].values * units.degC
        # wind_speed = df['speed'].values * units.knots
        # wind_dir = df['direction'].values * units.degrees
        # u,v = mpcalc.wind_components(wind_speed,wind_dir)
        v = df['VGRD'].values * units.knots
        u = df['UGRD'].values * units.degrees
        fig = plt.figure(figsize=(9,9))
        skew = SkewT(fig,rotation=45)
        skew.plot(p,T,'r')
        skew.plot(p,Td,'g')
        skew.plot_barbs(p,u,v)
        skew.ax.set_ylim(1050,100)
        skew.ax.set_xlim(-40,40)
        lcl_pressure,lcl_temperature = mpcalc.lcl(p[0],T[0],Td[0])
        skew.plot(lcl_pressure,lcl_temperature,'ko',markerfacecolor = 'black')
        prof = mpcalc.parcel_profile(p,T[0],Td[0]).to('degC')
        skew.plot(p,prof,'k',linewidth=2)
        skew.shade_cin(p,T,prof)
        skew.shade_cape(p,T,prof)
        skew.ax.axvline(0,color='c',linestyle='--',linewidth=2)
        skew.plot_dry_adiabats()
        skew.plot_moist_adiabats()
        skew.plot_mixing_lines()
        plt.title(k)
        plt.savefig('pic/{0}.png'.format(k))
        print(k)
        plt.close('all')
    except:
        pass
