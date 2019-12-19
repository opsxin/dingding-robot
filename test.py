import configparser
# from dingding.text import TextMsg
# from dingding.link import LinkMsg
# from dingding.markdown import MarkdownMsg
# from dingding.actioncard import ActionCardMsg
from dingding.feedcard import FeedCardMsg

from send_msg import requests_url

# 从配置文件获取钉钉 Webhook URL
cf = configparser.ConfigParser()
cf.read("config.ini")
dingding = cf.get("DEFAULT", "dingding")

# # text 测试
# if __name__ == "__main__":
#     content = "我就是我, "
#     content += "是不一样的烟火。"
#     phone_num = [12345678910, "23456789101"]
#     txt = TextMsg(content, phone_num)
#     my_data = txt.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# # Link 测试
# if __name__ == "__main__":
#     title = "时代的火车向前开"
#     content = "这个即将发布的新版本"
#     msg_url = "https://www.baidu.com"
#     link = LinkMsg(title, content, msg_url)
#     link.mod_pic_url(
#         "https://img.alicdn.com/tfs/TB1yL3taUgQMeJjy0FeXXXOEVXa-492-380.png")
#     my_data = link.conversion_json()
# print(requests_url.request_url(dingding, my_data))

# # Markdown 测试
# if __name__ == "__main__":
#     title = "杭州天气"
#     content = "杭州天气 #### 杭州天气 @156xxxx8827\n"
#     content += "> 9度，西北风1级，空气良89，相对温度73%\n\n"
#     phone_num = [12345, "12344"]
#     md = MarkdownMsg(title, content, phone_num)
#     my_data = md.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# # ActionCard 测试
# if __name__ == "__main__":
#     ac = ActionCardMsg(
#         "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
#         "![screenshot](@lADOpwk3K80C0M0FoA)")
#     btns = [{"1": "a"}, {"2": "b"}]
#     ac.button = btns
#     my_data = ac.conversion_json()
#     print(my_data)
#     print(requests_url.request_url(dingding, my_data))

# FeedCard 测试
if __name__ == '__main__':
    links = [[1, 2, 3], [4, "a"]]
    fc = FeedCardMsg(links)
    my_data = fc.conversion_json()
    print(my_data)
    print(requests_url.request_url(dingding, my_data))

