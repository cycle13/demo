import requests
import os
import time
import imageio
from datetime import datetime


session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


def downpic(name):
    url_pic = 'https://sprintars.riam.kyushu-u.ac.jp/images/{0}_sfc_asia_{1}.png'

    for i in range(1,65):
        time.sleep(1)
        print(i)
        if i <10:
            url = url_pic.format(name,"0"+str(i))
        else:
            url = url_pic.format(name,str(i))
        res = session.get(url,headers=headers)
        if not os.path.exists('data/' + now_data[0:4] + '/' + now_data[5:7] + '/' + now_data[8:10]+ '/' + name):
            os.makedirs('data/' + now_data[0:4] + '/' + now_data[5:7] + '/' + now_data[8:10]+ '/' + name)
        with open('data/' + now_data[0:4] + '/' + now_data[5:7] + '/' + now_data[8:10] + '/' + name+ '/' + str(i) + '.png','wb') as f:
            f.write(res.content)

def create_gif(image_list, gif_name, duration = 1.0):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def makegif(name):
    if not os.path.exists('pic/'+now_data[0:4]+'/'+now_data[5:7]+'/'+now_data[8:10]):
            os.makedirs('pic/'+now_data[0:4]+'/'+now_data[5:7]+'/'+now_data[8:10])
    img_names = ['data/'+now_data[0:4]+'/'+now_data[5:7]+'/'+now_data[8:10] + '/' + name+'/'+ str(i) + '.png' for i in range(1,65)]
    create_gif(img_names,'pic/'+now_data[0:4]+'/'+now_data[5:7]+'/'+now_data[8:10] +'/'+name+'.gif', duration=1.0)



names = ['pm25','pm10','conbc','conoc','consu','condu','consa','pptso2','pptdms']
for name in names:
    now_data = datetime.strftime(datetime.now(), '%Y-%m-%d')
    downpic(name)
    makegif(name)


