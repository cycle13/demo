import pywinauto
from pywinauto.application import Application
import time


pywinauto.keyboard.send_keys('%a')
time.sleep(2)
# pywinauto.mouse.move(coords=(0, 0))
pywinauto.mouse.press(button='left', coords=(0, 0))
time.sleep(2)
pywinauto.mouse.move(coords=(100, 100))
time.sleep(2)
pywinauto.mouse.release(button='left', coords=(100, 100))
pywinauto.keyboard.send_keys('{ENTER}')
app = Application(backend='uia').connect(process=9780)
# app = Application(backend="uia").start(r'D:\Program Files (x86)\Tencent\WeChat\WeChat.exe')
app.UntitledNotepad.type_keys("%FX")