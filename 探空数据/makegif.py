import imageio
import pandas as pd
import os


def create_gif(image_list, gif_name, duration = 1.0):
    '''
    :param image_list: 这个列表用于存放生成动图的图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param duration: 图像间隔时间
    :return:
    '''
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


fns = []
filelist = os.listdir(r'pic/')
for i in filelist:
    fns.append('county_image/'+i)


# fns = []
# for x in list(pd.date_range(start='2021-05-06', end='2021-05-07',freq='H')):
#     dt = x.strftime('%Y%m%d')
#     d = x.strftime('%H')
#     try:
#         dir = r'NC_H08_{}_{}00_L2ARP030_FLDK.02401_02401.nc'.format(dt,d)
#         dir1 = r'data/'+dir
#         if dir in filelist:
#             fns.append('county_image/{}_{}00.png'.format(dt,d))
#     except:
#         pass
# print(fns)
create_gif(fns,'gif/探空图.gif', duration=1.0)