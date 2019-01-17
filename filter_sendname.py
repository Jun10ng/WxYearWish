from test_send import FILTER_LIST
def check_send_name(friendList):
    """
    检查要发送的备注名
    :param friendList: 好友列表
    :return: 输出好友列表
    """
    for friend in friendList:
        print(friend)

def filter_sendname(friend):
    """
    修改好友名，因为每个人的备注名格式不一样
    如有的人 大学 学生会 张三
    而有的人 张三@学生会
    并且同一个人的通讯录的可能会有好几种不同的备注风格
    这个函数将  个性化的备注名 提取出 姓名
    仅修改 friend 数据结构中的 RemarkName 属性
    :param friend: 好友
    :return: friend(修改过）
    """
    #情况一：
    # 无备注名
    # 将昵称转换为备注
    if not friend['RemarkName']:
        friend['RemarkName']=friend['NickName']
        return friend
    else:
        remarkname = friend['RemarkName']

    # 情况二：
    # 备注名中包含 filterList 中的词汇
    for word in FILTER_LIST:
        if word in remarkname:
            remarkname = remarkname.replace(word,'')
            break

    # 情况三：
    # 备注名中有@，将删除@后面的所有字符
    if '@' in remarkname:
        pos = remarkname.index('@')
        remarkname = remarkname[:pos]


     # 情况二：
        # 只备注姓名的情况 ，例： RemarkName=张三 ，不修改
        # 判断条件是 备注名小于等于4个字
    if len(remarkname)<=4:
        friend['RemarkName']=remarkname
    return friend

def del_first_name(remarkname):
    """
    传入姓名
    为了太过生疏，去除姓，两个字的姓名不修改
    张大雷 修改为 大雷
    张雷  则不修改
    :param remarkname:姓名
    :return: 修改后的remarkname
    """
    if len(remarkname) == 3:
        return remarkname[1:]
    else:
        return remarkname

if __name__ == '__main__':
    remarkname1 ='张大雷'
    remarkname2 ='张雷'
    remarkname3 ='王乐老师'
    print(del_first_name(remarkname1))
    print(del_first_name(remarkname2))
    print(del_first_name(remarkname3))
