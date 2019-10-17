
#from dd_msg.text import TextMsg
#from dd_msg.link import LinkMsg
from dd_msg.markdown import MarkdownMsg
from send_msg import requests_url

# base_URL="https://wis.qq.com/weather/common?weather_type=observe|forecast_24h|air&source=pc"
# province="浙江省"
# city="杭州市"
# URL = base_URL + "&province=" + province + "&city=" + city

dingding="https://oapi.dingtalk.com/robot/send?access_token=48069c1f554a0ce416e85c3bbb381260b8c41352e1fb1af111b5a8d134cf0d00"

# text 测试
# if __name__ == "__main__":
#     txt = TextMsg(["this is test text"])
#     txt.add_content("2 chap")
#     my_data = txt.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# Link 测试
# if __name__ == "__main__":
#     link = LinkMsg("时代的火车向前开", ["这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？"], "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI", "https://dingtalkdoc.oss-cn-beijing.aliyuncs.com/images/0.0.154/1570863589633-c0c3ad21-7205-4787-b825-3c1231649a2d.png")
#     my_data = link.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# Markdown 测试
if __name__ == "__main__":
    md = MarkdownMsg("杭州天气", ["#### 杭州天气 @156xxxx8827\n"])
    md.add_content("> 9度，西北风1级，空气良89，相对温度73%\n\n")
    md.add_content("> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n")
    md.add_content("> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n")
    my_data = md.conversion_json()
    print(requests_url.request_url(dingding, my_data))