# dingding-robot
钉钉机器人 - 简化调用过程

## 说明
- 支持文本（Text）、链接（Link）、Markdown、ActionCard、FeedCard 消息类型
- 钉钉限制每个机器人每分钟最多发送 20 条

## 示例
### 1. 文本格式（Text）
```python
from dd_msg.text import TextMsg
from send_msg import requests_url


if __name__ == '__main__':
    txt = TextMsg("我就是我, ")
    txt.add_content("是不一样的烟火")
    my_data = txt.conversion_json()
    print(requests_url.request_url(dingding, my_data).text)
```

### 2. Markdown 格式
```python
from dd_msg.markdown import MarkdownMsg
from send_msg import requests_url


if __name__ == '__main__':
    md = MarkdownMsg("杭州天气", "#### 杭州天气\n")
    md.add_content("> 9度，西北风1级，空气良89，相对温度73%\n\n")
    md.add_content("> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n")
    md.add_content("> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n")
    my_data = md.conversion_json()
    print(requests_url.request_url(dingding, my_data).text)
```


> [钉钉开发文档](https://ding-doc.dingtalk.com/doc#/serverapi3/iydd5h)
