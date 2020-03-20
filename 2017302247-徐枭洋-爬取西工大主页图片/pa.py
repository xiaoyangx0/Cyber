import requests
import re
import sys
import os
import time


def Download():
    print("开始下载:")
    i = 1
    ymd = time.strftime("%Y%m%d", time.localtime(time.time()))   # 获取系统时间 年 月 日
    hms = time.strftime("%H%M%S", time.localtime(time.time()))         # 获取系统时间 小时 分钟 秒。 输出：120043
    path = str(ymd) + "_" + str(hms)
    os.mkdir("./" + path)
    print("目录已建立：" + path)

    urlfile = open("./url.txt", "r")
    lines = urlfile.readlines()
    for line in lines:
        line = line.strip()
        print("\n\n" + line)
        # 对下载部分进行异常处理
        try:
            # 用requests.get下载图片
            response = requests.get(line, headers=hea, verify=False,timeout=(12, 60))
            # 取response中二进制数据
            img = response.content
            print(response)
            #
            for j in range(1, 100):
                f = open("./" + path + "/" + str(i) + ".png", "wb")
                f.write(img)
                f.close
        # try中的语句如果出现异常，则执行except里面的代码
        except:
            # 输出出错的链接到errors.txt,并提示
            data2 = open("./errors.txt", "a", encoding='utf-8')
            data2.write(line + "\n")
            data2.close
            print("出现错误\n出错链接已保存至errors.txt")
            # 使用continue跳过本次出错的循环
            continue
        i += 1


def Getsource():
    inputurl = input('请输入网址(含http)：')
    html = requests.get(inputurl, headers=hea,verify=False, timeout=(72, 120))
    #
    # 转为utf-8编码
    html.encoding = 'utf-8'
    #
    # 输出获取的源码
    print("即将显示网页源码\n")
    time.sleep(2)
    print(html.text)
    #
    # 输出源码到文件
    data0 = open("./source.html", 'w+', encoding='utf-8')
    print(html.text, file=data0)
    data0.close()
    #
    # 延迟2秒后清屏
    time.sleep(2)
    # os.system('clear') #for Unix
    os.system('cls')  # for Windows
    #

    # PART 1 此为 正则表达式 部分。(写在''里面)。找到规律，利用正则，内容就可以出来 ps.注意表达式里的空格。
    text = re.findall('img src="(.*?)" /', html.text)
    #
    # 输出正则提取结果至文件
    data1 = open("./url.txt", "a", encoding='utf-8')
    for each in text:
        print("https://www.nwpu.edu.cn/"+ each)
        # 逐行写入保存到文本文件
        data1.write("https://www.nwpu.edu.cn/"+ each + "\n")





#           Main函数
hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

# 获取网页源码
Getsource()
#
# 下载文件
str_s1 = "\n是否下载文件? (y/n)\n选择："
while True:
    str_in1 = input(str_s1)
    if str_in1 in ('N', 'n'):
        break
    if str_in1 in ('Y', 'y'):
        Download()
        break
#
print("\n####成功运行！####")

