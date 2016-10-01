# BaiduCampusChecker
百度校招状态查询，定期检查百度校招的面试状态并发邮件通知，默认每小时检查一次并发邮件，如不想被邮件骚扰而只想要在状态改变时通知那么稍作修改即可。

Python2.x，无依赖库

# Usage
1. 登陆 [校招官网](http://talent.baidu.com/external/baidu/index.html)  后 F12在Console里输入 `document.cookie();` ，复制整一条（不含引号）到文件里的

		self.cookie = ""

2. 配置邮件发送人/接收人邮箱信息，默认配置了个发件人邮箱，所以你只需要填你的收件邮箱即可
	1. 收件人：你需要被通知的邮箱
	2. 发件人（默认不需要填写）：邮箱账号、密码，密码是SMTP密码，163、QQ等邮箱都需要去设置里开启。


3. 在后台跑起来就行了，建议放服务器上。

# License

**The MIT License**