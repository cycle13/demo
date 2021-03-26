from netCDF4 import Dataset
import pandas as pd




def data():
    aconc = Dataset(r'data/CCTM_ACONC_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    apmdiag = Dataset(r'data/CCTM_APMDIAG_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    conc = Dataset(r'data/CCTM_CONC_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    drydep = Dataset(r'data/CCTM_DRYDEP_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    wetdep1 = Dataset(r'data/CCTM_WETDEP1_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    data1 = pd.read_csv('data/Export_Output_7.csv',encoding='utf-8')
    ROW = aconc.dimensions['ROW'].size
    COL = aconc.dimensions['COL'].size
    lon = []
    lat = []

    for i in range(ROW):
        xl = []
        yl = []
        for j in range(COL):
            xl.append(data1['lons'][i*COL+j])
            yl.append(data1['lats'][i*COL+j])

        lon.append(xl)
        lat.append(yl)



    #计算PM2.5浓度
    ASO4IJ =conc.variables['ASO4I'][1][0]+conc.variables['ASO4J'][1][0]
    ANO3IJ =conc.variables['ANO3I'][1][0]+conc.variables['ANO3J'][1][0]
    ANH4IJ =conc.variables['ANH4I'][1][0]+conc.variables['ANH4J'][1][0]
    AORGPAIJ = 1.167*AORGPAIJ
    AORGAIJ =
    AORGBIJ =
    AECIJ =drydep.variables['AECI'][1][0]+drydep.variables['AECJ'][1][0]
    A25IJ =
    PM25 = ASO4IJ+ANO3IJ+ANH4IJ+AORGPAIJ+AORGAIJ+AORGBIJ+AECIJ +A25IJ


    # 计算PM10浓度
    ASOIL =
    ACORS =
    ASEAS =
    PM10 = ASOIL+ACORS+ASEAS


    # 计算SO2浓度
    SO2 = aconc.variables['SO2'][1][0]*64000/22.4

    # 计算NO2浓度
    NO2 = aconc.variables['NO2'][1][0]*46000/22.4

    # 计算O3浓度
    O3 = aconc.variables['O3'][1][0]*48000/22.4