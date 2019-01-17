"""
这是测试发送文件！！！
在运行send.py前 请先运行此文件
！！！！避免发送错误的备注！！！！
"""


import itchat
from get_all_friend import *
#自定义祝福语句
SEND_MSG_FORMAT = '新年快乐呀，{}'

#过滤词汇
FILTER_LIST = ['易班', '校会', '校研会']

if __name__ == '__main__':

    itchat.auto_login(True)

    friends = itchat.get_friends(update=True)[1:] #不包括自己

    test_send(friends,SEND_MSG_FORMAT)