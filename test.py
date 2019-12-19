import requests
import configparser
from dingding.text import TextMsg
# from dingding.link import LinkMsg
# from dingding.markdown import MarkdownMsg
# from dingding.actioncard import ActionCardMsg
# from dingding.feedcard import FeedCardMsg


# 从配置文件获取钉钉 Webhook URL
cf = configparser.ConfigParser()
cf.read("config.ini")
dingding = cf.get("DEFAULT", "dingding")

# requests 请求头
my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'application/json'
}

# text 测试
if __name__ == "__main__":
    content = "我就是我, 是不一样的烟火"
    phone_num = [12345678910]
    txt = TextMsg(content, phone_num)
    my_data = txt.conversion_json()
    if my_data:
        print(requests.post(dingding, data=my_data, headers=my_header))

# # Link 测试
# if __name__ == "__main__":
#     title = "时代的火车向前开"
#     content = "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林"
#     msg_url = "https://www.dingtalk.com/"
#     link = LinkMsg(title, content, msg_url)
#     link.mod_pic_url(
#         "http://1t.click/b6G")
#     my_data = link.conversion_json()
#     if my_data:
#         print(requests.post(dingding, data=my_data, headers=my_header))

# # Markdown 测试
# if __name__ == "__main__":
#     title = "杭州天气"
#     content = "杭州天气 #### 杭州天气 \n"
#     content += "> 9度，西北风1级，空气良89，相对温度73%\n\n"
#     content += "![screenshot](@lADOpwk3K80C0M0FoA) \n"
#     md = MarkdownMsg(title, content, at_all=True)
#     my_data = md.conversion_json()
#     if my_data:
#         print(requests.post(dingding, data=my_data, headers=my_header))

# # ActionCard 测试
# if __name__ == "__main__":
#     title = "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身"
#     content = "![screenshot](@lADOpwk3K80C0M0FoA) 乔布斯 20 年前想打造的苹果咖啡厅"
#     btn = [{"内容不错": "https://www.dingtalk.com/"}]
#     btns = [{"内容不错": "https://www.dingtalk.com/"}, {"不感兴趣": "https://www.dingtalk.com/"}]
#     ac = ActionCardMsg(title, content, btn)
#     ac.content = "![screenshot](http://1t.click/b6GF)修改内容"
#     ac2 = ActionCardMsg(title, content)
#     ac2.button = btns
#     my_data = ac.conversion_json()
#     my_data2 = ac2.conversion_json()
#     if my_data and my_data2:
#         print(requests.post(dingding, data=my_data, headers=my_header))
#         print(requests.post(dingding, data=my_data2, headers=my_header))

# # FeedCard 测试
# if __name__ == '__main__':
#     links = [[
#         "时代的火车向前开",
#         "https://www.dingtalk.com/",
#         "http://1t.click/b6GF"],
#         ["时代的火车向前开2",
#         "https://www.dingtalk.com/",
#         "http://1t.click/b6GF"]]
#     fc = FeedCardMsg(links)
#     my_data = fc.conversion_json()
#     if my_data:
#         print(requests.post(dingding, data=my_data, headers=my_header))

