# dingding-robot
钉钉机器人 - 简化调用过程。

## 说明
- 支持文本(Text)、链接(Link)、Markdown、ActionCard、FeedCard 消息类型
- 钉钉限制每个机器人每分钟最多发送 20 条

## 示例
### 1. 获取配置
```python
import configparser


cf = configparser.ConfigParser()
cf.read("config.ini")
dingding = cf.get("DEFAULT", "dingding")

# requests 请求头
my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'application/json'
}
```

### 2. 文本格式(Text)
```python
import requests
from dingding.text import TextMsg


if __name__ == "__main__":
    content = "我就是我, 是不一样的烟火"
    phone_num = [12345678910]
    txt = TextMsg(content, phone_num)
    my_data = txt.conversion_json()
    print(requests.post(dingding, data=my_data, headers=my_header))
```

### 3. Markdown 格式
```python
import requests
from dingding.markdown import MarkdownMsg


if __name__ == "__main__":
    title = "杭州天气"
    content = "杭州天气 #### 杭州天气 \n"
    content += "> 9度，西北风1级，空气良89，相对温度73%\n\n"
    md = MarkdownMsg(title, content, at_all=True)
    my_data = md.conversion_json()
    print(requests.post(dingding, data=my_data, headers=my_header))
```

### 4. 链接格式(Link)
```python
import requests
from dingding.link import LinkMsg


if __name__ == "__main__":
    title = "时代的火车向前开"
    content = "这个即将发布的新版本，创始人陈航(花名“无招”)称它为“红树林"
    msg_url = "https://www.dingtalk.com/"
    link = LinkMsg(title, content, msg_url)
    link.mod_pic_url("http://1t.click/b6G")
    my_data = link.conversion_json()
    print(requests.post(dingding, data=my_data, headers=my_header))
```

### 5. ActionCard 格式
```python
import requests
from dingding.actioncard import ActionCardMsg


if __name__ == "__main__":
    title = "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身"
    content = "![screenshot](@lADOpwk3K80C0M0FoA) 乔布斯 20 年前想打造的苹果咖啡厅"
    btn = [{"内容不错": "https://www.dingtalk.com/"}]
    btns = [{"内容不错": "https://www.dingtalk.com/"}, {"不感兴趣": "https://www.dingtalk.com/"}]
    ac = ActionCardMsg(title, content, btn)
    ac2 = ActionCardMsg(title, content)
    ac2.button = btns
    my_data = ac.conversion_json()
    my_data2 = ac2.conversion_json()
    print(requests.post(dingding, data=my_data, headers=my_header))
    print(requests.post(dingding, data=my_data2, headers=my_header))
```

### 6. FeedCard 格式
```python
import requests
from dingding.markdown import MarkdownMsg


if __name__ == '__main__':
    links = [["时代的火车向前开","https://www.dingtalk.com/","http://1t.click/b6GF"],
        ["时代的火车向前开2","https://www.dingtalk.com/","http://1t.click/b6GF"]]
    fc = FeedCardMsg(links)
    my_data = fc.conversion_json()
    print(requests.post(dingding, data=my_data, headers=my_header))
```

> [钉钉开发文档](https://ding-doc.dingtalk.com/doc#/serverapi3/iydd5h)


