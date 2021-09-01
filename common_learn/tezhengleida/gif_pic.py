import imageio
import pandas as pd




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

my_datatime = pd.date_range('12/01/2020', '12/31/2020')
img_names = ['image_file/'+str(i.strftime('%Y-%m-%d'))+'.png' for i in my_datatime]
print(img_names)
create_gif(img_names,'gif/雷达图12月.gif', duration=0.5)