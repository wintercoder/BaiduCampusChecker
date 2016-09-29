#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import time
from email.mime.text import MIMEText

import json
import os
import requests

requests.packages.urllib3.disable_warnings()


class Mail:
    def send(self, title, content):
        mail_user = "m18024160675@163.com"  # 发送者邮箱账号
        mail_pwd = "baidu233"   # 发送者邮箱密码(SMTP)
        mail_to = ""    # 目标的通知邮箱，可以跟自身相同

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
        # document.cookie() 整一条
        self.cookie = ""

        self.res_url = "http://talent.baidu.com/baidu/web/httpservice/getApplyRecordList?recruitType=1&_="
        self.s = requests.Session()
        self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
                        "Accept-Encoding": "gzip",
                        "Accept-Language": "zh-CN,zh;q=0.8",
                        "Referer": "http://talent.baidu.com/",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                        }
        self.s.headers = self.headers

    # 将输入的 Cookie 转换为字典类型
    def cookie_string_to_dict(self, cookiestr):
        cookie_dict = {}
        for line in cookiestr.split(";"):
            line_cache = line.split("=")
            cookie_key = line_cache[0]
            cookie_value = line_cache[1]
            if cookie_key != '':
                cookie_dict[cookie_key] = cookie_value
        return cookie_dict

    def check(self):
        now_time = (str(int(time.time() * 1000)))
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        rs = self.s.get(self.res_url + now_time, cookies=self.cookie_string_to_dict(self.cookie))
        # print rs.text

        json_str = json.loads(rs.text)
        result = json_str['applyRecordList'][0]['applyStatus']
        result = result.encode('utf-8')

        if result == "面试通过":
            Mail().send(result, result)
            os._exit()
        else:
            Mail().send("百度面试结果查询", result)

    def run(self):
        while True:
            self.check()
            time.sleep(60 * 30) # 半小时



if __name__ == "__main__":
    baidu = BaiduTalent()
    baidu.run()
