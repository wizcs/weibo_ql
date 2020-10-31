#
# THIS FILE IS WIZ WU's PROJECT
# wbql.py - 一个未经专业处理的脚本程序，用于微博抢楼评论
# 2020.10.30
# this code is free, But the program may not be free
# For Preventing legal risks , IS LICENSED UNDER GPL3.0
# circularwiz@outlook.com
# Version ：1.0
#


import requests
import time

# 以下为个人设置部分，具体方法见文档：
c_text = ''       #要输入的要求文字
cookies_1 = '     '               #见文档介绍
url = ''  # 抢楼微博移动端链接
floor = [38, 41]  # 待抢楼层，数组形式
# try_times = 6  # 每层楼尝试发送评论数
default_frequency = 3  # 初始刷新频率/S
# 其他初始化变量：
now_floor = 1
headers = {'cookie': cookies_1}  # 个人登录cookies
q1 = url.find('l/')
weibo_mid = url[(q1+2):]


def Frequency(flag_floor):  # 刷新频率计算小函数
    if(flag_floor > 100):
        return default_frequency
    elif(flag_floor > 20):
        return (flag_floor/200)*default_frequency
    else:
        return (flag_floor/10)*0.1


def Spider(url, headers):
    r = requests.get(url, headers=headers)
    page_text = r.text
    return page_text


def Get_content_num(page_text):  # 获得当前content num
    n0 = page_text.find('comments_count')
    t0 = page_text[(n0+17):(n0+25)]
    n1 = t0.find(',')
    try:
        return(int(t0[:n1]))
    except ValueError:
        print('ERROR:这是一个关于cookies的bug1号')


def Get_weibo_st(page_text):  # 获得微博x-xsrf-token
    w1 = page_text.find('st:')
    w2 = page_text[w1:(w1+16)]
    w3 = w2.find(',')
    w4 = w2[5:(w3-1)]
    return w4


def Leave_comment(c_text, weibo_mid, weibo_st):  # 进行评论
    url2 = 'https://m.weibo.cn/api/comments/create'
    payload = {'content': c_text, 'mid': weibo_mid,
               'st': weibo_st, '_spr': 'screen:1920x1080'}
    requests.post(url2, data=payload, headers=headers)


# 以上为基本运行函数，以下为逻辑程序部分
# 具体就是在到达接近楼层floor[try_goals]前不断改变刷新频率直到最终20-10开始准备发送评论，一次发送2-3条，以最大概率并且“稍微体面的”获得楼层


def main_p1(try_goals):  # （递归）一个凭本事刷出来的抢楼方法：越临近目标楼发的越多，一共6个求别人别乱删除,否则严重失效,且建立在人多的情况下。
    page_text = Spider(url, headers)
    now_floor = Get_content_num(page_text)
    weibo_st = Get_weibo_st(page_text)

    if(now_floor < floor[try_goals]):
        flag_floor = floor[try_goals] - now_floor
        if((flag_floor < 7) and (flag_floor >= 3)):
            Leave_comment(c_text+'!!!!!!', weibo_mid, weibo_st)
            time.sleep(0.02)
            Leave_comment(c_text+'!!!!!', weibo_mid, weibo_st)
            time.sleep(0.04)
            Leave_comment(c_text+'!!!!', weibo_mid, weibo_st)
        if((flag_floor < 14) and (flag_floor >= 7)):
            Leave_comment(c_text+'!!!', weibo_mid, weibo_st)
            Leave_comment(c_text+'!!', weibo_mid, weibo_st)
        if((flag_floor < 28) and (flag_floor >= 14)):
            Leave_comment(c_text+'!', weibo_mid, weibo_st)
        if(flag_floor <= 2):  # 基本不可能吧这个
            Leave_comment(c_text+'!!!!!!!!', weibo_mid, weibo_st)
            Leave_comment(c_text+'!!!!!!!!!', weibo_mid, weibo_st)
        time.sleep(Frequency(flag_floor))
    else:
        try_goals = try_goals + 1  # 换到下一个目标
        print('开始抢下一楼层' + str(try_goals))
    main_p1(try_goals)


def main_p2(try_goals, last_flag_floor):  # 接近之后隔一发一,每一次获得最少1/2的几率
    page_text = Spider(url, headers)
    now_floor = Get_content_num(page_text)
    weibo_st = Get_weibo_st(page_text)
    if(now_floor < floor[try_goals]):
        flag_floor = floor[try_goals] - now_floor
        flag_floor_2 = last_flag_floor-flag_floor
        if((flag_floor < 16) and (flag_floor_2 > 2)):         #
            Leave_comment(c_text+'!'+str(now_floor), weibo_mid, weibo_st)
            last_flag_floor = flag_floor
            last_flag_floor = flag_floor
        time.sleep(Frequency(flag_floor))
        print(now_floor)
    else:
        try_goals = try_goals + 1  # 换到下一个目标
        last_flag_floor = 16
        print('开始抢下一楼层' + str(try_goals))
    main_p2(try_goals, last_flag_floor)


main_p2(0, 16)
