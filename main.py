#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import smtplib
import sys
import time
import urllib2
from email.mime.text import MIMEText


class Mail:
    @staticmethod
    def send(title, content):
        mail_user = "m18024160675@163.com"  # 邮箱账号
        mail_pwd = "baidu233"  # 邮箱密码(SMTP)
        mail_to = ""  # 目标的通知邮箱，可以跟自身相同

        msg = MIMEText(content, 'plain', 'utf-8')

        msg["Subject"] = title
        msg["From"] = mail_user
        msg["To"] = mail_to

        s = smtplib.SMTP("smtp.163.com", timeout=30)
        s.login(mail_user, mail_pwd)
        s.sendmail(mail_user, mail_to, msg.as_string())
        s.close()


class BaiduTalent:
    def __init__(self):
        # Console里的 document.cookie() 整一条
        self.cookie = ""
        self.res_url = "http://talent.baidu.com/baidu/web/httpservice/getApplyRecordList?recruitType=1&_="
        self.opener = urllib2.build_opener()

    def check(self):
        now_time = (str(int(time.time() * 1000)))
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        new_cookie = self.cookie
        # new_cookie = self.cookie.replace(self.cookie.split('Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=')[1], now_time) # 确保一直最新

        self.opener.addheaders = [
            ('Accept', 'application/json, text/javascript, */*; q=0.01'),
            ('X-Requested-With', 'XMLHttpRequest'),
            ("Accept-Encoding", "gzip, deflate, sdch"),
            ("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6"),
            ('Referer', 'http://talent.baidu.com/external/baidu/index.html'),
            ("User-Agent",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"),
            ("Cookie", new_cookie)
        ]
        url = self.res_url + now_time
        result = self.opener.open(url)

        # print result.read()
        try:
            json_str = json.loads(result.read())
            result = json_str['applyRecordList'][0]['applyStatus']
            result = result.encode('utf-8')

            if "面试通过" in result:
                Mail.send(result, result)
                sys.exit(0)
            else:
                Mail.send("百度面试结果查询", result)
        except ValueError:
            Mail.send("百度面试结果查询-Cookie过期", 'Cookie过期')
            sys.exit(0)

    def run(self):
        while True:
            self.check()
            # 一小时查询一次
            time.sleep(60 * 60)


if __name__ == "__main__":
    baidu = BaiduTalent()
    baidu.run()
