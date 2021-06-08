import cv2 as cv
import imageio
import numpy as np



def create_gif(image_list, gif_name, duration = 1.0):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def pic_l(ls):
    src = cv.imread(ls)
    txt = '晴颸 浮阳'
    AddText = src.copy()
    cv.putText(AddText,txt,(230,410),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),10)
    res = np.hstack([src,AddText])
    cv.imshow('text',res)
    cv.waitKey()

img_names = [r'gfs\2021\04\T2m\27\2700_'+ str(i) + '.png' for i in range(1,65)]
for ls in img_names:
    pic_l(ls)
create_gif(img_names,'PM25动图.gif', duration=0.5)

