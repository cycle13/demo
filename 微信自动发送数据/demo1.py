import win32api
import win32con
import win32gui
import pandas as pd
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


if __name__ == '__main__':
    while True:
        FindWindow("李世林")
        paste_img(r"D:\Program Files\pycharm\微信自动发送数据\1.png")
        fasong()
        setText("aString")
        fasong()
        CloseWindow("李世林")
        time.sleep(2)