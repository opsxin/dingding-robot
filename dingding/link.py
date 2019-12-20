"""Link 类型
"""
import json

from .base import Base


class LinkMsg(Base):
    __msgtype = "link"

    def __init__(self, title, content, msg_url, pic_url=""):
        """初始化

        :param title: 标题 
        :param content: 消息内容
        :param msg_url: 点击消息跳转的 URL
        :param pic_url: 图片 URL
        """
        self._title = title
        self._content = content
        self._msg_url = msg_url
        self._pic_url = pic_url

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        """修改标题
        """
        if title.strip():
            self._title = title
        else:
            print("标题不能为空")

    def mod_msg_url(self, url):
        """修改跳转 URL
        """
        if url.strip():
            self._msg_url = url
        else:
            print("消息 URL 不能为空")

    def mod_pic_url(self, url):
        """修改图片 URL
        """
        self._pic_url = url

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        if len(self._content) == 0 or len(self._title) == 0 or len(self._msg_url) == 0:
            print("内容不能为空")
            return
        else:
            data = {
                'msgtype': self.__msgtype, 'link': {
                    'text': str(self._content), 'title': str(self._title),
                    'picUrl': self._pic_url, 'messageUrl': self._msg_url
                }
            }
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    title = "时代的火车向前开"
    content = "这个即将发布的新版本"
    msg_url = "https://www.baidu.com"
    link = LinkMsg(title, content, msg_url)
    link.mod_pic_url(
        "https://img.alicdn.com/tfs/TB1yL3taUgQMeJjy0FeXXXOEVXa-492-380.png")
    print(link.conversion_json())

