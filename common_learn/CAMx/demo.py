import PseudoNetCDF as pnc


pncf = pnc.pncopen(r"data/CAMx.v7.00.36.12.MPICH3.20210404.avrg.grd01.nc").copy()
# Computing a derived variable
pncf.eval("NOX=NO+NO2", inplace=True)
# To make outfile VERDI-compatible...
del pncf.Conventions
del pncf.variables['x']
del pncf.variables['y']
del pncf.variables['latitude']
del pncf.variables['longitude']
pncf.save("test_out.nc")