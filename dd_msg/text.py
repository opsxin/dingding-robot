"""Text 类型
"""
import sys
import json


class TextMsg(object):
    def __init__(self, content, at_mobile=[], at_all=False):
        """
        初始化

        :param content: 消息内容
        :param at_mobile: @ 用户
        :param _at_all: @ 所有人
        """
        self._msgtype = "text"
        self.content = content
        self.at_mobile = at_mobile
        self._at_all = at_all

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

    def add_at_num(self, num):
        """
        添加 @ 的手机号码
        """
        self.at_mobile.append(num)

    def del_at_num(self, num):
        """
        删除手机号码
        """
        try:
            self.at_mobile.remove(num)
        except ValueError:
            print("删除的手机号码不存在")

    def set_at_all(self, at_values=False):
        """
        设置是否 @ 所有人
        """
        if isinstance(at_values, bool):
            self._at_all = at_values
        else:
            print("set_at_all 的值只能 True 或 False")

    def conversion_json(self):
        """
        转换内容为 JSON 格式
        """
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            data = {'msgtype': self._msgtype, 'text': {'content': self.content},
                    'at': {'atMobiles': self.at_mobile}, 'isAtAll': self._at_all
                    }
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    txt = TextMsg("测试发送 TXT 内容。")
    txt.add_content("追加内容。")
    # txt.del_content()
    txt.add_content("设置新内容。")
    txt.add_at_num("12345678910")
    # txt.del_at_num("12345678910")
    txt.set_at_all(True)
    print(txt.conversion_json())
