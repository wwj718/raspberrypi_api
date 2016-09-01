#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time
from flask import Flask
from flask_cors import CORS, cross_origin

#from flask_socketio import SocketIO, emit
from flask_sockets import Sockets # pip install flask-sockets

app = Flask(__name__)
CORS(app)
#app.config['HOST'] = '0.0.0.0'
#socketio = SocketIO(app)
sockets = Sockets(app)

# 对硬件的操作参考：http://blog.mangolovecarrot.net/2015/04/20/raspi-study01/ , 感谢 mango 同学
# 指定GPIO口的选定模式为GPIO引脚编号模式（而非主板编号模式）
#RPi.GPIO.setmode(RPi.GPIO.BCM)

# 指定GPIO14（就是LED长针连接的GPIO针脚）的模式为输出模式
# 如果上面GPIO口的选定模式指定为主板模式的话，这里就应该指定8号而不是14号。
#RPi.GPIO.setup(14, RPi.GPIO.OUT)

# 循环10次
@app.route('/led_up')
def led_up():
    RPi.GPIO.output(14, True)
    return 'ok'

@app.route('/led_down')
def led_down():
    RPi.GPIO.output(14, False)
    return 'ok'
# 闪啊闪
@app.route('/led_up_down')
def led_up_down():
  for i in range(0, 5):
    # 让GPIO14输出高电平（LED灯亮）
    RPi.GPIO.output(14, True)
    # 持续一段时间
    time.sleep(0.5)
    # 让GPIO14输出低电平（LED灯灭）
    RPi.GPIO.output(14, False)
    # 持续一段时间
    time.sleep(0.5)
  return 'ok'

# 闪啊闪
@app.route('/led_up_down')
def led_up_down():
  for i in range(0, 5):
    # 让GPIO14输出高电平（LED灯亮）
    RPi.GPIO.output(14, True)
    # 持续一段时间
    time.sleep(0.5)
    # 让GPIO14输出低电平（LED灯灭）
    RPi.GPIO.output(14, False)
    # 持续一段时间
    time.sleep(0.5)
  return 'ok'

@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(message)
        ws.send(message)


# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
#RPi.GPIO.cleanup()


#if __name__ == '__main__':
#    #app.run(host='0.0.0.0',port='5000')
#    socketio.run(app,host="0.0.0.0")
if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
