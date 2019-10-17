"""Markdown 类型"""

import json


class MarkdownMsg(object):
    def __init__(self, title, content, at_mobile=[], at_all=False):
        self.__msgtype = "markdown"
        self.title = title
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
            print("True 或 False")

    def conversion_json(self):
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            data = {'msgtype': self.__msgtype, 'markdown': {'text': ' '.join(self.content)
                , 'title': self.title}, 'at': {'atMobiles': self.at_mobile, 'isAtAll': self.__at_all}}
            return json.dumps(data)