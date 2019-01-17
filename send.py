"""
这是真实的发送代码文件！！！
在运行本程序前 请先运行test_send.py文件
！！！！避免发送错误的备注！！！！
"""

from get_all_friend import *

# 导入过滤词汇 和 祝福语格式
from test_send import FILTER_LIST,SEND_MSG_FORMAT

if __name__ == '__main__':

    itchat.auto_login(True)

    friends = itchat.get_friends(update=True)[1:] #不包括自己

    send(friends,SEND_MSG_FORMAT)
