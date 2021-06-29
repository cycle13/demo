from diamond5 import Diamond5
import pandas as pd
from skewt import Skew_T
from tkinter.filedialog import askopenfilename
import datetime
from pathlib import Path

# fp = askopenfilename()
# date = str(Path(fp)).split('\\')[-1].split('.')[0]
# dtime = datetime.datetime.strptime(date, '%Y%m%d%H%M%S')
# d = Diamond5(fp)
df = pd.read_excel('tankong.xlsx',sheet_name=None)



for k in df.keys():
    try:
        data = pd.read_excel('tankong.xlsx',sheet_name=k)

        skewt = Skew_T(data.pressure.values, data.TMP.values, td=data.dewpoint.values,
                       u=data.UGRD.values, v=data.VGRD.values, alt=data.HGT.values * 10, station='E112,N37.5',time=k)
        skewt.save('pic/{0}.png'.format(k))
        print(k)
    except:
        pass

