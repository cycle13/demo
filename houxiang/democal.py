import os
import datetime


# Set working directory
metDir = r'D:\Program Files\pycharm\houxiang\Temp\arl'
outDir = r'D:\Program Files\pycharm\houxiang\Temp\HYSPLIT'
workingDir = r'TrajStat/working'
os.chdir(workingDir)
print('Current directory: ' + os.getcwd())

# Set parameters
lon = '112.35'
lat = '37.75'
shour = '00'
heights = ['100.0', '500.0', '1000.0']
hnum = len(heights)
hours = '-48'
vertical = '0'
top = '10000.0'

# Set meteorological data files
fns = []
fn = r'current7days.t00z'
fns.append(fn)

# Set start/end time
stime = datetime.datetime(2021, 5, 20)

# Write CONTROL file
ctFile = './CONTROL'
print(stime.strftime('%Y-%m-%d ') + shour + ':00')
ctf = open(ctFile, 'w')
ctf.write(stime.strftime('%y %m %d ') + shour + "\n")
ctf.write(str(hnum) + '\n')
for i in range(0, hnum):
    ctf.write(lat + ' ' + lon + ' ' + heights[i] + '\n')
ctf.write(hours + '\n')
ctf.write(vertical + '\n')
ctf.write(top + '\n')
fnnum = len(fns)
ctf.write(str(fnnum) + '\n')
for i in range(0, fnnum):
    ctf.write(metDir + '/' + '\n')
    ctf.write(fns[i] + '\n')
ctf.write(outDir + '/' + '\n')
outfn = stime.strftime('traj_%Y%m%d.txt')
print(outfn)
ctf.write(outfn)
ctf.close()

# Calculate trajectories
os.system(r'D:\TrajStat\working\hyts_std.exe')

print('Finish...')
