# weibo_ql
一个用于微博抢楼的小脚本 v1.0

使用方法：
1.进入并登录https://m.weibo.cn，请保持移动端页面
2.随便进入一条原创微博，其地址格式为url = 'https://m.weibo.cn/detail/XXXXXXXXXXX'这样的
3.用edge浏览器或者chrome，在这个微博页面进入F12.点击网络功能，并刷新网页，找到cookies，如图所示，复制cookies的冒号之后所有内容到cookies字符串内
4.c_text 字符串输入要用的文字
5.url = 'https://m.weibo.cn/detail/XXXXXXXXXXX'  
在抢楼微博发布之后，用此时所说的移动端网页进入此界面，格式如上将链接复制到url字符串内
6.输入其他需要输入的东西，比如目标楼层之类的

