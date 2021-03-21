import cv2 as cv
import numpy as np

# 读入图片
src = cv.imread('data/1.png')

# 调用cv.putText()添加文字
text = "."
AddText = src.copy()
cv.putText(AddText, text, (281, 174), cv.FONT_HERSHEY_COMPLEX, 0.2, (0, 0, 0), 5)

# 将原图片和添加文字后的图片拼接起来
res = np.hstack([src, AddText])

# 显示拼接后的图片
cv.imshow('text', res)
cv.waitKey()
