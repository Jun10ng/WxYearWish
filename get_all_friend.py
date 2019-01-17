import time,itchat
from filter_sendname import *
from test_send import *

# 测试发送函数
def test_send(friendList,SEND_MSG_FORMAT):
    """
    测试发送，并不是发送消息，而是在屏幕输出将要发送的消息
    带备注名的祝福语句
    :param friendList:好友列表
    :param SEND_MSG_FORMAT: 祝福语句格式
    :return: 在屏幕输出将要发送的消息带备注名的祝福语句
    """
    for friend in friendList:
        #自定义修改备注
        friend = filter_sendname(friend)
        SEND_MSG_NAME = friend['RemarkName']

        #去除三个字名字的姓
        SEND_MSG_NAME=del_first_name(SEND_MSG_NAME)
        SEND_MSG = SEND_MSG_FORMAT.format(SEND_MSG_NAME)

        print(SEND_MSG)

# 正式发送消息函数
def send(friendList,SEND_MSG_FORMAT):
    """
     正式发送
     正式发送
     正式发送
     :param friendList:好友列表
     :param SEND_MSG_FORMAT: 祝福语句格式
     :return: 发送给好友带备注名的祝福语句
     """
    for friend in friendList:
        # 自定义修改备注
        friend = filter_sendname(friend)
        SEND_MSG_NAME = friend['RemarkName']

        # 去除三个字名字的姓
        SEND_MSG_NAME = del_first_name(SEND_MSG_NAME)
        SEND_MSG = SEND_MSG_FORMAT.format(SEND_MSG_NAME)
        # 发送
        itchat.send(SEND_MSG,friend['UserName'])
        # 每条消息发送有0.5延迟
        time.sleep(.5)