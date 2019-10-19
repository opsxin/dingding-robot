import configparser
# from dd_msg.text import TextMsg
# from dd_msg.link import LinkMsg
# from dd_msg.markdown import MarkdownMsg
# from dd_msg.actioncard import ActionCardMsg
# from dd_msg.feedcard import FeedCardMsg
from send_msg import requests_url

# 从配置文件获取钉钉 Webhook URL
config_path = "config.ini"
cf = configparser.ConfigParser()
cf.read(config_path)
dingding = cf.get("DEFAULT", "dingding")

# # text 测试
# if __name__ == "__main__":
#     txt = TextMsg("我就是我, ")
#     txt.add_content("是不一样的烟火")
#     # txt.set_at_all(True)
#     my_data = txt.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# # Link 测试
# if __name__ == "__main__":
#     link = LinkMsg(
#         "时代的火车向前开",
#         "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。",
#         "https://img.alicdn.com/tfs/TB1jFpqaRxRMKJjy0FdXXaifFXa-497-133.png")
#     link.add_content(
#         "而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？"
#     )
#     link.set_pic_url("https://img.alicdn.com/tfs/TB1jFpqaRxRMKJjy0FdXXaifFXa-497-133.png")
#     my_data = link.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# # Markdown 测试
# if __name__ == "__main__":
#     md = MarkdownMsg("杭州天气", "#### 杭州天气\n")
#     md.add_content("> 9度，西北风1级，空气良89，相对温度73%\n\n")
#     md.add_content("> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n")
#     md.add_content("> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n")
#     # md.add_at_num("12345678910")
#     # md.set_at_all(True)
#     my_data = md.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# # ActionCard 测试
# if __name__ == "__main__":
#     ac = ActionCardMsg(
#         "乔布斯 20 年前想打造一间苹果咖啡厅", 
#         "![screenshot](@lADOpwk3K80C0M0FoA)")
#     ac.add_content("### 乔布斯 20 年前想打造的苹果咖啡厅")
#     ac.add_content("Apple Store 的设计正从原来满满的科技感走向生活化")
#     ac.add_button("baidu", "https://www.baidu.com")
#     # ac.add_button("qq", "https://www.qq.com")
#     my_data = ac.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

# # FeedCard 测试
# if __name__ == '__main__':
#     fc = FeedCardMsg()
#     fc.add_link(
#         "时代的火车向前开", "https://www.dingtalk.com", "https://www.dingtalk.com/"
#     )
#     fc.add_link(
#         "时代的火车向前开2", "https://www.dingtalk.com", "https://www.dingtalk.com/"
#     )
#     my_data = fc.conversion_json()
#     print(requests_url.request_url(dingding, my_data))

