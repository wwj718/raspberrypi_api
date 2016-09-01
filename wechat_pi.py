#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
from wxbot import WXBot
import requests
#bot_api="http://192.168.0.108:8000/get_response"
led_server = 'http://127.0.0.1:5000/'

#import BaiduYuyin as pby
#YOUR_APP_KEY = "BElGG5nsGL8oevAa3gMzMk4Y"
#YOUR_SECRET_KEY = "uVla1FdpQ2HgmojeY9e6pobrS3lRGaeY"
#tts = pby.TTS(app_key=YOUR_APP_KEY, secret_key=YOUR_SECRET_KEY)


class MyWXBot(WXBot):
    def _led(self,msg,user_input,action):
        response = '正在{}'.format(user_input)
        self.send_msg_by_uid(response, msg['user']['id'])
        url = led_server+action
        requests.get(url)
        response = '完成{}'.format(user_input)
        self.send_msg_by_uid(response, msg['user']['id'])


    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            user_input = msg["content"]["data"]
            #payload={"user_input":user_input}
            # 读出来
            #print(user_input)
            #print(type(user_input)) # unicode
            #tts.say(user_input.encode("utf-8")) # encode decode
            #response = requests.get(bot_api,params=payload).json()["response"]
            if '关' in user_input:
                self._led(msg,user_input,'led_down')
            if '开' in user_input:
                self._led(msg,user_input,'led_up')
            if '闪' in user_input:
                self._led(msg,user_input,'led_up_down')
            #print response
            #print(type(response)) # unicode

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()
