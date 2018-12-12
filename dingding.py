#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=7f25442478beca503735e4f8e4bad95e615b3cdc672a1d834e53d9ba3c75f73e"

def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                "1881***1223"
            ],
            "isAtAll": False
        }
    }
    ## 这是python2的语法；python3的要修改
    #print requests.post(api_url,json.dumps(json_text),headers=headers).content
    print(requests.post(api_url,json.dumps(json_text),headers=headers).content)

if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
