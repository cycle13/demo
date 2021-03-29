from netCDF4 import Dataset


def data(i):
    aconc = Dataset(r'data/CCTM_ACONC_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    apmdiag = Dataset(r'data/CCTM_APMDIAG_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
    #1、计算PM2.5浓度
    APOMI = aconc.variables['ALVPO1I'][i][0] + aconc.variables['ASVPO1I'][i][0] + aconc.variables['ASVPO2I'][i][0] + aconc.variables['APOCI'][i][0] +aconc.variables['APNCOMI'][i][0]
    APOMJ = aconc.variables['ALVPO1J'][i][0]+ aconc.variables['ASVPO1J'][i][0] + aconc.variables['ASVPO2J'][i][0] + aconc.variables['APOCJ'][i][0] +aconc.variables['ASVPO3J'][i][0] + aconc.variables['AIVPO1J'][i][0] + aconc.variables['APNCOMJ'][i][0]
    ASOMI = aconc.variables['ALVOO1I'][i][0] + aconc.variables['ALVOO2I'][i][0] + aconc.variables['ASVOO1I'][i][0] + aconc.variables['ASVOO2I'][i][0]
    ASOMJ = aconc.variables['AISO1J'][i][0]+ aconc.variables['AISO2J'][i][0]+ aconc.variables['AISO3J'][i][0] +aconc.variables['AMT1J'][i][0] + aconc.variables['AMT2J'][i][0] + aconc.variables['AMT3J'][i][0]+ aconc.variables['AMT4J'][i][0]+aconc.variables['AMT5J'][i][0]+ aconc.variables['AMT6J'][i][0] + aconc.variables['AMTNO3J'][i][0]+aconc.variables['AMTHYDJ'][i][0] + aconc.variables['AGLYJ'][i][0]+ aconc.variables['ASQTJ'][i][0]\
            +aconc.variables['AORGCJ'][i][0]+ aconc.variables['AOLGBJ'][i][0] + aconc.variables['AOLGAJ'][i][0]+aconc.variables['ALVOO1J'][i][0] + aconc.variables['ALVOO2J'][i][0] + aconc.variables['ASVOO1J'][i][0]+ aconc.variables['ASVOO2J'][i][0]+aconc.variables['ASVOO3J'][i][0] + aconc.variables['APCSOJ'][i][0] + aconc.variables['AAVB1J'][i][0] + aconc.variables['AAVB2J'][i][0]+aconc.variables['AAVB3J'][i][0] + aconc.variables['AAVB4J'][i][0]
    AOMI = APOMI+ ASOMI
    AOMJ = APOMJ + ASOMJ
    ATOTI = aconc.variables['ASO4I'][i][0]+aconc.variables['ANO3I'][i][0]+aconc.variables['ANH4I'][i][0]+aconc.variables['ANAI'][i][0]+aconc.variables['ACLI'][i][0]+aconc.variables['AECI'][i][0]+AOMI+aconc.variables['AOTHRI'][i][0]
    ATOTJ = aconc.variables['ASO4J'][i][0]+aconc.variables['ANO3J'][i][0]+aconc.variables['ANH4J'][i][0]+aconc.variables['ANAJ'][i][0]+aconc.variables['ACLJ'][i][0]+aconc.variables['AECJ'][i][0]+AOMJ+aconc.variables['AOTHRJ'][i][0]+aconc.variables['AFEJ'][i][0]+aconc.variables['ASIJ'][i][0]+aconc.variables['ATIJ'][i][0]+aconc.variables['ACAJ'][i][0]+aconc.variables['AMGJ'][i][0]+aconc.variables['AMNJ'][i][0]+aconc.variables['AALJ'][i][0]+aconc.variables['AKJ'][i][0]
    ATOTK = aconc.variables['ASOIL'][i][0]+aconc.variables['ACORS'][i][0]+aconc.variables['ASEACAT'][i][0]+aconc.variables['ACLK'][i][0]+aconc.variables['ASO4K'][i][0]+aconc.variables['ANO3K'][i][0]+aconc.variables['ANH4K'][i][0]
    PM25AC = apmdiag.variables['PM25AC'][i][0]
    PM25AT = apmdiag.variables['PM25AT'][i][0]
    PM25CO = apmdiag.variables['PM25CO'][i][0]
    PM25_TOT = ATOTI*PM25AT+ATOTJ*PM25AC+ATOTK*PM25CO
    PM25_CL = aconc.variables['ACLI'][i][0] * PM25AT + aconc.variables['ACLJ'][i][0] * PM25AC + aconc.variables['ACLK'][i][0] * PM25CO
    PM25_EC = aconc.variables['AECI'][i][0] * PM25AT + aconc.variables['AECJ'][i][0] * PM25AC
    # PM25_NA = aconc.variables['ANAI'][i][0] * PM25AT + aconc.variables['ANAJ'][i][0] * PM25AC + aconc.variables['ANAK'][i][0] * PM25CO
    PM25_NA = aconc.variables['ANAI'][i][0] * PM25AT + aconc.variables['ANAJ'][i][0] * PM25AC
    PM25_NH4 = aconc.variables['ANH4I'][i][0] * PM25AT + aconc.variables['ANH4J'][i][0] * PM25AC + aconc.variables['ANH4K'][i][0] * PM25CO
    PM25_NO3 = aconc.variables['ANO3I'][i][0] * PM25AT + aconc.variables['ANO3J'][i][0] * PM25AC + aconc.variables['ANO3K'][i][0] * PM25CO
    # PM25_OC = aconc.variables['AOCI'][i][0] * PM25AT + aconc.variables['AOCJ'][i][0] * PM25AC
    # PM25_SOIL = aconc.variables['ASOILJ'][i][0] * PM25AC + aconc.variables['ASOIL'][i][0] * PM25CO
    PM25_SOIL = aconc.variables['ASOIL'][i][0] * PM25CO
    PM25_SO4 = aconc.variables['ASO4I'][i][0] * PM25AT + aconc.variables['ASO4J'][i][0] * PM25AC + aconc.variables['ASO4K'][i][0] * PM25CO
    PM25 = PM25_TOT-(PM25_CL+PM25_EC+PM25_NA+PM25_NH4+PM25_NO3+PM25_SOIL+PM25_SO4)
    # return PM25

    # # 2、计算PM10浓度
    PM10AC = apmdiag.variables['PM10AC'][i][0]
    PM10AT = apmdiag.variables['PM10AT'][i][0]
    PM10CO = apmdiag.variables['PM10CO'][i][0]

    PM10 = ATOTI*PM10AT+ATOTJ*PM10AC+ATOTK*PM10CO
    # return PM10

    # 3、计算SO2浓度
    SO2 = aconc.variables['SO2'][i][0]*64000/22.4
    # return SO2

    # 4、计算NO2浓度
    NO2 = aconc.variables['NO2'][i][0]*46000/22.4
    # return NO2

    # 5、计算O3浓度
    O3 = aconc.variables['O3'][i][0]*48000/22.4
    return PM25,PM10,SO2,NO2,O3