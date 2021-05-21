import shapefile
from matplotlib.path import Path
from matplotlib.patches import PathPatch


shpfile = 'Documents/Export_Output_2.shp'
sf = shapefile.Reader(shpfile, encoding='utf-8')
print(sf.shapeRecords)
for shape_rec in sf.shapeRecords():
    print(shape_rec.record)