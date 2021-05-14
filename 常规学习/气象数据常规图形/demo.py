import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('data/气象数据1.xls')
fig = plt.figure()
ax1 = plt.subplot(2,1,1)
plt.plot(df['UNIX_TIMESTAMP(vt)'],df['TMP_2'])
plt.plot(df['UNIX_TIMESTAMP(vt)'],df['DPT_2'])
ax2 = plt.subplot(2,1,2)
plt.plot(df['UNIX_TIMESTAMP(vt)'],df['TMP_850'])
plt.plot(df['UNIX_TIMESTAMP(vt)'],df['PRMSL_0'])
plt.show()