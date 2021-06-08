import requests
import datetime
import os
import time
import imageio

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

urls = 'http://www.data.jma.go.jp/gmd/env/kosa/fcst/en/img/surf/as/{0}00_kosafcst-s_en_as.png'


def create_gif(image_list, gif_name, duration=0.5):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def jap(num, yes):
    name_pic = []
    for i in range(0, num):
        timedata = (datetime.datetime(int(yes[0:4]), int(yes[4:6]), int(yes[6:8]), 0, 0) + datetime.timedelta(
            hours=i * 3)).strftime("%Y%m%d%H")
        url = urls.format(timedata)
        print(url)
        res = session.get(url, headers=headers)
        if res.status_code == 200:
            if not os.path.exists('jap/' + yes[0:4] + '/' + yes[4:6] + '/' + yes[6:8]):
                os.makedirs('jap/' + yes[0:4] + '/' + yes[4:6] + '/' + yes[6:8])
            with open('jap/' + yes[0:4] + '/' + yes[4:6] + '/' + yes[6:8] + '/' + timedata + '.png', 'wb') as f:
                f.write(res.content)
            name_pic.append(timedata + '.png')

    if not os.path.exists('gif/' + yes[0:4] + '/' + yes[4:6]):
        os.makedirs('gif/' + yes[0:4] + '/' + yes[4:6])
    dir_list1 = os.listdir('jap/' + yes[0:4] + '/' + yes[4:6] + '/' + yes[6:8])
    img_names = ['jap/' + yes[0:4] + '/' + yes[4:6] + '/' + yes[6:8] + '/' + i for i in name_pic]
    create_gif(img_names, 'gif/' + yes[0:4] + '/' + yes[4:6] + '/' + yes[6:8] + '日' + '沙尘预测图.gif', duration=0.5)
    time.sleep(86380)


while True:
    yestoday = datetime.datetime.now().strftime("%Y%m%d")
    try:
        jap(32, yestoday)
    except:
        time.sleep(59)
    time.sleep(86380)