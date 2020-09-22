#coding=utf-8

import urllib.request
import re
import os
import urllib
import calendar
import time

import ssl 
#----------------------------------------------------------------------
#   防止出错,不然会报encode_chunked=req.has_header('Transfer-encoding'))错误
ssl._create_default_https_context = ssl._create_unverified_context
#----------------------------------------------------------------------

#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码  
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    #print(html)
    return html.decode('GB2312')
 
#解决下载不完全情况
#网路很不稳定时，会抛出错误，这是因为第二次重新下载时依然出现下载不完全的情况。
#我们可以使用 递归 的方法，即每次下载不完全时重新下载解决这个问题。    
def auto_down(url,filename):
    try:
        urllib.request.urlretrieve(url,filename)
    except urllib.request.ContentTooShortError:
        print('Network conditions is not good.Reloading.')
        auto_down(url,filename)


def getImg(html,http,path):
    reg = r'href=".+?\.png"'
    #reg=r'href=".+?\"
    imgre = re.compile(reg)
    imglist= imgre.findall(html)#表示在整个网页中过滤出所有图片的地址，放在imglist中
    print(imglist)
    x = 0
#def saveImg(path) 
   # 将图片保存到D:\\test文件夹中，如果没有test文件夹则创建   
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'      #保存在test路径下  
    for imgurl in imglist:
        imgurl=imgurl[6:]
        imgurl=imgurl[:-1]  #为了截取图片的名称
        imgurl_1=http+imgurl #合成图片下载地址
        print(imgurl_1)
        auto_down(imgurl_1,'{}{}.png'.format(paths,imgurl))
        #urllib.request.urlretrieve(imgurl_1,'{}{}.png'.format(paths,imgurl))  #打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串 
        x = x + 1  
    return imglist
#http="http://222.195.136.24/chart/kma/data_keep/2009/2009-03/20090302/"
web="http://222.195.136.24/chart/kma/data_keep/"
DateNOW = time.strftime('%Y-%m-%d',time.localtime(time.time())) #用于比较日期大小

for year in range(2019,2019+1):
	for mon in range(1,12+1):
		m = "%02d" % mon
		monthRange = calendar.monthrange(year,mon)
		for day in range(1,monthRange[1]+1):
			d = "%02d" % day
			ReadingDate = str(year)+"-"+str(m)+"-"+str(d)
			if ReadingDate <= DateNOW: #日期在今天及之前，则读取
				print("#------------------------------------------------------------------------------------------#")
				print("#					Reading Date is:",ReadingDate)
				print("#------------------------------------------------------------------------------------------#")
				http=web+str(year)+"/"+str(year)+"-"+str(m)+"/"+str(year)+str(m)+str(d)+"/"
				#save path
				html = getHtml(http)#获取该网址网页详细信息，得到的html就是网页的源代码
				path = './png/'+str(year)+"/"+str(year)+"-"+str(m)+"/"+str(year)+str(m)+str(d)+"/"
				print('#					Data Storaged Directory is: ',path)
				print("#------------------------------------------------------------------------------------------#")
				print("\n")
				print (getImg(html,http,path)) #从网页源代码中分析并下载保存图片
				print("\n")
			else:
				print("Datas Reading All Done!")
				break
				

