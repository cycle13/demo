import win32api
import win32con
import win32gui
import pandas as pd
import os
import time
import win32clipboard as w
from io import BytesIO
import requests
import json
from win32com.client import Dispatch, DispatchEx
from PIL import ImageGrab, Image
import uuid
import xlwt
import openpyxl
import openpyxl.styles
from openpyxl.styles import PatternFill
from datetime import datetime
from pymouse import PyMouse


# 获取句柄
def FindWindow(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    print("找到群聊窗口：%x" % win)
    if win != 0:
        win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        win32gui.ShowWindow(win, win32con.SW_SHOW)
        win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 100, 100, 300, 300, win32con.SWP_SHOWWINDOW)
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(1)
    else:
        print('请注意：找不到【%s】这个人（或群），请激活窗口！' % chatroom)
        exit()

# 关闭窗口
def CloseWindow(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    #print("找到关闭窗口：%x" % win)
    time.sleep(3)
    win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)


# 把文字放到剪切板
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


# 图片转化成BPM格式图片
def paste_img(file_img):
    # 把图片写入image变量中
    # 用open函数处理后，图像对象的模式都是 RGB
    image = Image.open(file_img)

    # 声明output字节对象
    output = BytesIO()

    # 用BMP (Bitmap) 格式存储
    # 这里是位图，然后用output字节对象来存储
    image.save(output, 'BMP')

    # BMP图片有14字节的header，需要额外去除
    data = output.getvalue()[14:]

    # 关闭
    output.close()
    # DIB: 设备无关位图(device-independent bitmap)，名如其意
    # BMP的图片有时也会以.DIB和.RLE作扩展名
    # 设置好剪贴板的数据格式，再传入对应格式的数据，才能正确向剪贴板写入数据
    setImage(data)


# 把图片放到剪切板
def setImage(data):  # 写入剪切板

    w.OpenClipboard()
    try:
        # Unicode tests
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_DIB, data)
    except:
        traceback.print_exc()
    finally:
        w.CloseClipboard()



# 模拟ender
def ender():
    win32api.keybd_event(13,0,0,0)  #ender键位码是13
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

# 模拟ctrl+v
def ctrlV():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,0,0,0)  #v键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

# 模拟ctrl+a
def altA():
    win32api.keybd_event(18, 0, 0, 0)    #Alt
    win32api.keybd_event(65,0,0,0) #s
    win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)


# 模拟alt+s
def altS():
    win32api.keybd_event(18, 0, 0, 0)    #Alt
    win32api.keybd_event(83,0,0,0) #s
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)

# 粘贴发送
def fasong():
    ctrlV()
    altS()

# 还在开发中
def jieimage():
    FindWindow("王彦军")
    altA()

# 还在开发中
def mouse_click():
    m = PyMouse()
    # a = m.position()  # 获取当前坐标的位置
    # m.move(50, 500)  # 鼠标移动到(x,y)位置
    # a = m.position()
    m.click(50, 50)  # 移动并且在(x,y)位置左击
    m.move(500, 500)
    # m.click(300, 300, 2)  # (300,300)位置右击


# 获取文件夹下的所有图片
def get_file(image):
    file_name = os.listdir(image)
    return file_name


# 每发完一次删除文件夹下的图片
def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)



def daily_push(file_dir,l,name):
    FindWindow(name)
    setText(l)
    fasong()
    for i in get_file(file_dir):
        paste_img(file_dir + "\\" + i)
        fasong()
    CloseWindow(name)
    # 删除文件夹下所有文件
    # del_files(file_dir)
    time.sleep(2)


if __name__ == '__main__':
    file_dir = "D:/Program Files/pycharm/微信自动发送数据/万柏林/image"
    l = "【点位空气质量变化情况】\n     {}，西山点位：AQI为{}，{}" \
        "，首要污染物：{}，在全市11个标准站中排名第{}，六城区排名第{}。\n     PM2.5实时浓度为{}μg/m³，" \
        "今日{}时平均浓度为{}μg/m³；\n     PM10实时浓度为{}μg/m³，今日{}时平均浓度为{}μg/m³" \
        "；\n     SO2实时浓度为{}μg/m³，今日{}时平均浓度为{}μg/m³；\n     NO2实时浓度为{}μg/m³，" \
        "今日{}时平均浓度为{}μg/m³；\n     从变化趋势图来看，西山点位{}呈{}趋势。\n      当前气象条件：{}，相对湿度{}，预计未来几个小时我区空气质量以{}为主。".format("2020年11月4日 6时", "95", "二级良",
                                                                          "PM10", "十一", "六", "40", "1-6", "30", "140",
                                                                          "1-6", "114", "15",
                                                                          "1-6", "14", "69", "1-6", "62", "、".join(['PM2.5浓度','PM10浓度','SO2浓度','NO2浓度']),"上升","西南风一级",
                                                                          "47%", "二级")
    file_dir1 = "D:/Program Files/pycharm/微信自动发送数据/万柏林/image1"
    m = "【万柏林区{}微观站日报】\n各位领导，{}我区各乡/街" \
        "道 {} 浓度排名和微观点位颗粒物浓度后十位排名，具体情况如下表所示：\n当前气" \
        "象条件：{}，相对湿度{}，预计未来几个小时我区空气质量以{}为主。 ".format("2020年11月3日", "2020年11月3日", "PM10",
                                                       "南风一级", "54%", "三级")

    file_dir2 = "D:/Program Files/pycharm/微信自动发送数据/万柏林/image2"
    n = "各位领导，{}我区各乡街的空气质量日报如下，请查收。".format("2020年11月3日")

    file_dir3 = "D:/Program Files/pycharm/微信自动发送数据/万柏林/image3"
    o = "【万柏林区{}空气质量日报】\n{}，万柏林区综合" \
        "指数为{}，在太原市六城区中排名{}。太原市全市AQI为{}，{}，首要" \
        "污染物：{}。万柏林区全区AQI值为{}，{}，首要污染物：{}，在太原" \
        "市六城区中排名{}。在太原市11个标准站中，西山点位AQI值为{}，排名" \
        "{}。\n当前气象条件：{}，相对湿度{}，预计未来几个小时我区空气质量以{}为主。".format("2020年11月3日","2020年11月3日","3.22",
                                                               "第一","70","二级良","NO2","56","二级良","PM10","第一","56","第二",
                                                               "南风二级","38%","三级")

    file_dir4 = "D:/Program Files/pycharm/微信自动发送数据/万柏林/image4"
    p = "【夜间累计浓度变化情况】\n{}时，西山点位累计AQI为{}，{}，首" \
        "要污染物：{}，今日{}时PM2.5平均浓度为{}μg/m³；今日{}时PM10平均浓" \
        "度为{}μg/m³。\n 当前气象条件：{}，相对湿度{}，预计未来几个小时我区空气质量以" \
        "{}为主。".format("2020年11月2日20","44","一级优","无","1-20","9","1-20","44","西北风二级","30%","一级")
    daily_push(file_dir, l, "李世林")