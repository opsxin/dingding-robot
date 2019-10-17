"""Link 类型"""

import json 


class LinkMsg(object):
    def __init__(self, title, content, msg_url, pic_url=""):
        self.__msgtype = "link"
        self.title = title
        self.content = content
        self.msg_url = msg_url
        self.pic_url = pic_url
    
    def add_content(self, content):
        self.content.append(content)
    
    def del_content(self):
        self.content.clear()

    def conversion_json(self):
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            data = {'msgtype': self.__msgtype, 'link': {'text': ' '.join(self.content)
                , 'title': self.title, 'picUrl': self.pic_url, 'messageUrl': self.msg_url}}
            return json.dumps(data)