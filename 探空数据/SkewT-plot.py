from skewt import SkewT

import os,sys
Dir, filename = os.path.split(os.path.abspath(sys.argv[0]))
Dir = Dir + '\\'

S=SkewT.Sounding("./58457.txt")
S.plot_skewt(imagename='58457', color='b')