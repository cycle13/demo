

# 确定纬度的计算方式，偏差较大
# ROW = data.dimensions['ROW'].size
# COL = data.dimensions['COL'].size
# XCELL = data.XCELL/1000
# YCELL = data.YCELL/1000
# XCEN = data.XCENT
# YCEN = data.YCENT
# XLON = XCELL*COL/(2*111)
# YLON = YCELL*ROW /(2*111*np.cos(YCEN))
# lons = np.linspace(XCEN-XLON,XCEN+XLON,COL)
# lats = np.linspace(YCEN-YLON,YCEN+YLON,ROW)

# # 动态计算经纬度
# ROW = data.dimensions['ROW'].size
# COL = data.dimensions['COL'].size
# XCELL = data.XCELL/1000
# YCELL = data.YCELL/1000
# XCEN = data.XCENT
# YCEN = data.YCENT
# s = (np.pi/18)*6371
# YLON = (YCELL*(ROW/2))/s
# latt = []
# for i in range(ROW):
#     latt.append((YCEN-YLON)+i*(2*YLON)/ROW)
# lons = []
# for k in latt:
#     xl = []
#     XLON = XCELL * COL / (2 * s * np.cos(k))
#     for i in range(COL):
#         xl.append((XCEN - XLON)+i*(2*XLON)/COL)
#     lons.append(xl)
# lats = []
# for j in range(COL):
#     lats.append(latt)
# lon, lat = np.meshgrid(lons, lats)

