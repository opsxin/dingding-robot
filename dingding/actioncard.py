"""ActionCard 类型
"""
import json

from .base import Base


class ActionCardMsg(Base):
    __msgtype = "actionCard"

    def __init__(self, title, content, btns=[], btn_orientation=False, hide_avatar=False):
        """初始化

        :param title: 标题 
        :param content: 消息内容(Markdown 格式)
        :param btns: 消息按钮, [{"title": "URL"}, {"title": "URL"}]
        :param btn_orientation: 0-按钮竖直排列，1-按钮横向排列
        :param hide_avatar: 0-正常发消息者头像，1-隐藏发消息者头像
        """
        self._title = title
        self._content = content
        self._btns = []
        for btn in btns:
            for title, action_url in btn.items():
                if title.strip() and action_url.strip():
                    new_btn = {'title': title, 'actionURL': action_url}
                    self._btns.append(new_btn)
                else:
                    raise ValueError("标题或 URL 不能为空")
        self._btn_orientation = btn_orientation
        self._hide_avatar = hide_avatar

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

    @property
    def button(self):
        return self._btns

    @button.setter
    def button(self, btns):
        """修改按钮
        """
        self._btns.clear()
        for btn in btns:
            for title, action_url in btn.items():
                if title.strip() and action_url.strip():
                    new_btn = {'title': title, 'actionURL': action_url}
                    self._btns.append(new_btn)
                else:
                    raise ValueError("标题或 URL 不能为空")

    def set_btn_orientation(self, btn_orientation=False):
        """按钮显示方式
        """
        if isinstance(btn_orientation, bool):
            self._btn_orientation = btn_orientation
        else:
            raise TypeError("类型为 bool")

    def set_hide_avatar(self, hide_avatar=False):
        """发送者头像显示方式
        """
        if isinstance(hide_avatar, bool):
            self._hide_avatar = hide_avatar
        else:
            raise TypeError("类型为 bool")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        data = {}
        if len(self._content) == 0:
            raise ValueError("内容不能为空")
        elif len(self._title) == 0:
            raise ValueError("标题不能为空")
        else:
            if len(self._btns) == 1:
                data = {'msgtype': self.__msgtype, 'actionCard': {
                    'text': self._content, 'title': self._title, 'hideAvatar': int(self._hide_avatar),
                    'btnOrientation': int(self._btn_orientation), 'singleTitle': self._btns[0]['title'],
                    'singleURL': self._btns[0]['actionURL']}}
            elif len(self._btns) > 1:
                data = {'msgtype': self.__msgtype, 'actionCard': {
                    'text': self._content, 'title': self._title, 'hideAvatar': int(self._hide_avatar),
                    'btnOrientation': int(self._btn_orientation), 'btns': self._btns, }}
            else:
                raise ValueError("按钮不能为空")
            return json.dumps(data)


# 测试
if __name__ == "__main__":
    title = "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身"
    content = "![screenshot](@lADOpwk3K80C0M0FoA) 乔布斯 20 年前想打造的苹果咖啡厅"
    btns = [{"内容不错": "https://www.dingtalk.com/"},
            {"不感兴趣": "https://www.dingtalk.com/"}]
    ac = ActionCardMsg(title, content, btns)
    ac.content = "![screenshot](http://1t.click/b6GF)修改内容"
    print(ac.conversion_json())

