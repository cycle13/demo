import shapefile
from matplotlib.path import Path
from matplotlib.patches import PathPatch


def shp2clip(originfig, ax, shpfile, region):
    sf = shapefile.Reader(shpfile, encoding='utf-8')
    print(sf.shapeRecords)
    for shape_rec in sf.shapeRecords():
        print(shape_rec.record)
        if shape_rec.record[0] == region:  ####这里需要找到和region匹配的唯一标识符，record[]中必有一项是对应的。
            vertices = []
            codes = []
            pts = shape_rec.shape.points
            prt = list(shape_rec.shape.parts) + [len(pts)]
            for i in range(len(prt) - 1):
                for j in range(prt[i], prt[i + 1]):
                    vertices.append((pts[j][0], pts[j][1]))
                codes += [Path.MOVETO]
                codes += [Path.LINETO] * (prt[i + 1] - prt[i] - 2)
                codes += [Path.CLOSEPOLY]
            clip = Path(vertices, codes)
            clip = PathPatch(clip, transform=ax.transData)
    for contour in originfig.collections:
        contour.set_clip_path(clip)

    return clip