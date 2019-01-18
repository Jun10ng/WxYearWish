# WxYearWish
基于Itchat库的一个小脚本。 能根据微信好友的备注发送带有备注名的祝福语。能根据不同的好友备注风格更改。
支持根据自己的备注风格 更改过滤规则


修改test_send.py 文件中的 SEND_MSG_FORMAT 变量可自定义祝福语句 SEND_MSG_FORMAT中的{}代指对方姓名

如备注风格为 张大雷@XX公司 张小雷@厦门
在test_send.py 文件中的 FILTER_LIST 变量中添加希望去除的词汇（如XX公司，厦门）既可。

可自定义备注名过滤规则！
备注名过滤规则在 filter_sendname.py中filter_sendnam（）函数中
各位根据自己的备注风格修改相关代码即可。

为了避免发生三个字太过生疏，在filter_sendname.py添加了del_first_name（）函数 去除姓氏（只有三字姓名情况下才会去除姓氏，如张大雷会变成大雷）

提供测试发送功能，运行test_send.py 将在屏幕输出发送给所有好友的消息（并不会真正发送）


正式发送文件为send.py
运行send.py才会正式发送消息。请在务必先运行测试发送文件，避免悲剧发生！！！！！

![image](https://github.com/Jun10ng/WxYearWish/blob/master/test_send_img.png)
