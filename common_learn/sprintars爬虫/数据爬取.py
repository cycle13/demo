import requests
import os
import time
import imageio
from datetime import datetime


session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
url = 'https://sprintars.riam.kyushu-u.ac.jp/forecast.html'
url_pm25 = 'https://sprintars.riam.kyushu-u.ac.jp/forecast_movie_pm25_easia.html'
url_pic = 'https://sprintars.riam.kyushu-u.ac.jp/images/pm25_easia_{}.png'
res = session.get(url,headers = headers)
res = session.get(url_pm25,headers=headers)
now_data = datetime.strftime(datetime.now(), '%Y-%m-%d')
for i in range(1,65):
    time.sleep(1)
    if i <10:
        url = url_pic.format("0"+str(i))
    else:
        url = url_pic.format(str(i))
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+now_data):
        os.makedirs('data/'+now_data)
    with open('data/'+ now_data +'/'+ str(i) + '.png', 'wb') as f:
        f.write(res.content)

def create_gif(image_list, gif_name, duration = 1.0):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

if not os.path.exists('county_image/'+now_data):
    os.makedirs('county_image/'+now_data)
img_names = ['data/'+ now_data +'/'+ str(i) + '.png' for i in range(1,65)]
create_gif(img_names,'county_image/'+ now_data +'/'+'PM25动图.gif', duration=1.0)