"""Text 类型"""
import sys
import json


class TextMsg(object):
    def __init__(self, content, at_mobile=[], at_all=False):
        self.__msgtype = "text"
        self.content = content
        self.at_mobile = at_mobile
        self.__at_all = at_all

    def add_content(self, content):
        self.content.append(content)

    def del_content(self):
        self.content.clear()

    def set_at_all(self, at_values):
        if type(at_values) == bool:
            self.__at_all = at_values
        else:
            sys.exit("set_at_all 的值只能 True 或 False")

    def conversion_json(self):
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            data = {'msgtype': self.__msgtype, 'text': {'content': ' '.join(self.content)},
                    'at': {'atMobiles': self.at_mobile}, 'isAtAll': self.__at_all}
            return json.dumps(data)


# 测试
if __name__ == "__main__":
    txt = TextMsg(["this is test text"])
    txt.add_content("test 2")
    txt.del_content()
    txt.add_content("test 3")
    txt.conversion_json()
