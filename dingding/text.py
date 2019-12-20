"""Text 类型
"""
import json

from .base import Base


class TextMsg(Base):
    __msgtype = "text"

    def __init__(self, content, at_mobile=[], at_all=False):
        """初始化

        :param content: 消息内容
        :param at_mobile: @ 用户
        :param at_all: @ 所有人
        """
        self._content = content
        self._at_mobile = []
        for num in at_mobile:
            if isinstance(num, str):
                self._at_mobile.append(num)
            elif isinstance(num, int):
                self._at_mobile.append(str(num))
            else:
                raise TypeError("类型为 str")
        if isinstance(at_all, bool):
            self._at_all = at_all
        else:
            raise TypeError("类型为 bool")

    @property
    def phone_num(self):
        return self._at_mobile

    @phone_num.setter
    def phone_num(self, nums):
        """修改手机号码

        Args: 
            num: 手机号码(String)
        """
        self._at_mobile.clear()
        for num in nums:
            if isinstance(num, str):
                self._at_mobile.append(num)
            elif isinstance(num, int):
                self._at_mobile.append(str(num))
            else:
                raise TypeError("类型为 str")

    def set_at_all(self, at_values):
        """设置是否 @ 所有人

        Args: 
            at_values(bool)
        """
        if isinstance(at_values, bool):
            self._at_all = at_values
        else:
            raise TypeError("类型为 bool")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        if len(self._content) == 0:
            raise ValueError("内容不能为空")
        else:
            data = {'msgtype': self.__msgtype, 'text': {'content': str(self._content)},
                    'at': {'atMobiles': self._at_mobile, 'isAtAll': self._at_all}}
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    content = "我就是我, "
    content += "是不一样的烟火。"
    phone_num = [12345678910, "23456789101"]
    txt = TextMsg(content, phone_num)
    print(txt.conversion_json())

