# 提醒
项目不再维护，推荐使用[gpiozero](https://gpiozero.readthedocs.io/en/stable/)

# raspberrypi_api
把树莓派的硬件功能作为web api

![](https://raw.githubusercontent.com/wwj718/gif_bed/master/ledf96a0f7d.png)

# 原因
*  近期公司有一个有趣的项目，希望用乐高玩具式的可视化编程工具来操控硬件
*  树莓派操控硬件需要有root权限，作为服务之后则没有限制
*  解耦

# 架构
*  初期效用flask作为web框架
*  把led_server视为下位机，api视为指令集

# 使用
我的树莓派当前ip为：192.168.0.106

### 启动服务
sudo python led_server.py

### 控制
可以在浏览器或命令行里打开api接口（动作）

*  点亮红灯： curl 192.168.0.106/led_up
*  熄灭红灯： curl 192.168.0.106/led_down
*  闪啊闪  ： curl 192.168.0.106/led_up_down

#### 在网页中用js控制
```javascript
xmlhttp=new XMLHttpRequest();
xmlhttp.open("GET","http://192.168.0.106/led_up_down",true);
xmlhttp.send();
```


# 微信控制
和此前的[wechat_bot](https://github.com/wwj718/wechat_bot)关联即可

# todo
*  权限
 *  先用`?key=xxx`
*  websocket
 *  长连接
   *  双向通信  
 *  浏览器中js可操作
 *  python实现：  
   *  [WebSocket-for-Python](https://github.com/Lawouach/WebSocket-for-Python)
   *  [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
   *  [flask-sockets](https://github.com/kennethreitz/flask-sockets) （暂时选择这个）

# done
*  cors 
  *  可以用js控制硬件
