"""Link 类型
"""
import sys
import json


class LinkMsg(object):
    def __init__(self, title, content, msg_url, pic_url=""):
        """
        初始化

        :param title: 标题 
        :param content: 消息内容
        :param msg_url: 点击消息跳转的 URL
        :param pic_url: 图片显示的 URL
        """
        self._msgtype = "link"
        self.title = title
        self.content = content
        self.msg_url = msg_url
        self.pic_url = pic_url

    def mod_title(self, title):
        """
        修改标题
        """
        if not title.strip():
            self.title = title
        else:
            print("title 不能为空")

    def add_content(self, content):
        """
        添加消息内容
        """
        self.content += content

    def del_content(self):
        """
        清空消息内容
        """
        self.content = ""

    def mod_msg_url(self, url):
        """
        修改跳转 URL
        """
        if not url.strip():
            self.msg_url = url
        else:
            print("msg_url 不能为空")

    def set_pic_url(self, url):
        """
        设置图片 URL
        """
        self.pic_url = url

    def conversion_json(self):
        """
        转换内容为 JSON 格式
        """
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            data = {
                'msgtype': self._msgtype, 'link': {
                    'text': self.content, 'title': self.title,
                    'picUrl': self.pic_url, 'messageUrl': self.msg_url
                }
            }
            return json.dumps(data)

# 测试
if __name__ == '__main__':
    link = LinkMsg(
        "时代的火车向前开", "这个即将发布的新版本",
        "https://www.baidu.com"
    )
    link.add_content("追加内容。")
    # link.del_content()
    link.add_content("设置新内容。")
    link.set_pic_url("https://img.alicdn.com/tfs/TB1yL3taUgQMeJjy0FeXXXOEVXa-492-380.png")
    print(link.conversion_json())
    