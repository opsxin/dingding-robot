"""Markdown 类型
"""
import json

from .text import TextMsg


class MarkdownMsg(TextMsg):
    __msgtype = "markdown"

    def __init__(self, title, content, at_mobile=[], at_all=False):
        """初始化

        :param title: 标题 
        :param content: 消息内容
        :param at_mobile: @ 用户
        :param at_all: @ 所有人
        """
        self._title = title
        super().__init__(content, at_mobile, at_all)

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
            raise ValueError("标题不能为空")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        if len(self._title) == 0:
            raise ValueError("标题不能为空")
        elif len(self._content) == 0:
            raise ValueError("内容不能为空")
        else:
            data = {'msgtype': self.__msgtype, 'markdown': {
                'text': str(self._content), 'title': str(self._title)}, 'at': {
                'atMobiles': self._at_mobile, 'isAtAll': self._at_all}}
            return json.dumps(data)


# 测试
if __name__ == "__main__":
    title = "杭州天气"
    content = "杭州天气 #### 杭州天气 \n"
    md = MarkdownMsg(title, content, at_all=True)
    md.content = "> 9度，西北风1级，空气良89，相对温度73%\n\n"
    print(md.conversion_json())

