"""ActionCard 类型
"""
import sys
import json

from .base import Base


class ActionCardMsg(Base):
    __msgtype = "actionCard"

    def __init__(self, title, content, btns=[], btn_orientation=0, hide_avatar=0):
        """初始化

        :param title: 标题 
        :param content: 消息内容（Markdown 格式）
        :param btns: 消息按钮
        :param btn_orientation: 0-按钮竖直排列，1-按钮横向排列
        :param hide_avatar: 0-正常发消息者头像，1-隐藏发消息者头像
        """
        self._title = title
        self._content = content
        self._btns = btns
        self._btn_orientation = btn_orientation
        self._hide_avatar = hide_avatar

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        """修改标题
        """
        if not title.strip():
            self._title = title
        else:
            print("标题不能为空")

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
                if title.strip() or action_url.strip():
                    new_btn = {'title': title, 'actionURL': action_url}
                    self._btns.append(new_btn)
                else:
                    print("按钮标题和跳转 URL 不能为空")

    def set_btn_orientation(self, btn_orientation=0):
        """按钮显示方式
        """
        if btn_orientation == 0 or btn_orientation == 1:
            self._btn_orientation = btn_orientation
        else:
            print("按钮显示的值只能 0 或 1")

    def set_hide_avatar(self, hide_avatar=0):
        """发送者头像显示方式
        """
        if hide_avatar == 0 or hide_avatar == 1:
            self._hide_avatar = hide_avatar
        else:
            print("隐藏头像的值只能 0 或 1")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        data = {}
        if len(self._content) == 0:
            sys.exit("内容不能为空")
        else:
            if len(self._btns) == 1:
                data = {'msgtype': self.__msgtype, 'actionCard': {
                    'text': self._content, 'title': self._title, 'hideAvatar': self._hide_avatar,
                    'btnOrientation': self._btn_orientation, 'singleTitle': self._btns[0]['title'],
                    'singleURL': self._btns[0]['actionURL']}}
            elif len(self._btns) > 1:
                data = {'msgtype': self.__msgtype, 'actionCard': {
                    'text': self._content, 'title': self._title, 'hideAvatar': self._hide_avatar,
                    'btnOrientation': self._btn_orientation, 'btns': self._btns, }}
            else:
                sys.exit("按钮不能为空")
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    ac = ActionCardMsg(
        "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
        "![screenshot](@lADOpwk3K80C0M0FoA)")
    btns = [{"1": "a"}, {"2": "b"}]
    ac.button = btns
    print(ac.conversion_json())

