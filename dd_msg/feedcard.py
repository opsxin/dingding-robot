"""FeedCard 类型
"""
import sys
import json


class FeedCardMsg(object):
    def __init__(self):
        """初始化

        :param links: 消息链接
        """
        self._msgtype = "feedCard"
        self.links = []

    def add_link(self, title, message_url, pic_url):
        """添加链接
        """
        if title.strip() or message_url.strip() or pic_url.strip():
            new_link = {
                'title': title, 'messageURL': message_url, 'picURL': pic_url
            }
            self.links.append(new_link)
        else:
            print("title 和 URL 不能为空")

    def del_link(self, index):
        """删除链接
        """
        try:
            self.links.pop(index)
        except IndexError:
            print("删除范围为 0 -", len(self.links)-1)
        except TypeError:
            print("index 只能为数字")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        if len(self.links) < 1:
            sys.exit("链接不能为空")
        else:
            data = {'msgtype': self._msgtype, 'feedCard': {
                'links': self.links}
            }
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    fc = FeedCardMsg()
    fc.add_link("1", "2", "3")
    fc.add_link("2", "3", "4")
    # fc.del_link("c")
    print(fc.conversion_json())
