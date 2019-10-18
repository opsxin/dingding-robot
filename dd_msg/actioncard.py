"""ActionCard 类型
"""
import sys
import json


class ActionCardMsg(object):
    def __init__(
            self, title, content, btn_orientation=0, hide_avatar=0):
        """初始化

        :param title: 标题 
        :param content: 消息内容（Markdown 格式）
        :param btns: 消息按钮
        :param btn_orientation: 0-按钮竖直排列，1-按钮横向排列
        :param hide_avatar: 0-正常发消息者头像，1-隐藏发消息者头像
        """
        self._msgtype = "actionCard"
        self.title = title
        self.content = content
        self.btns = []
        self.btn_orientation = btn_orientation
        self.hide_avatar = hide_avatar

    def mod_title(self, title):
        """修改标题
        """
        if not title.strip():
            self.title = title
        else:
            print("title 不能为空")

    def add_content(self, content):
        """添加消息内容
        """
        self.content += content

    def del_content(self):
        """清空消息内容
        """
        self.content = ""

    def mod_content(self, content):
        """修改消息内容
        """
        self.del_content()
        self.add_content(content)

    def add_button(self, title, action_url):
        """添加按钮
        """
        if title.strip() or action_url.strip():
            new_btn = {'title': title, 'actionURL': action_url}
            self.btns.append(new_btn)
        else:
            print("按钮标题和跳转 URL 不能为空")

    def del_button(self, index):
        """删除按钮
        """
        try:
            self.btns.pop(index)
        except IndexError:
            print("删除范围为 0 -", len(self.btns)-1)
        except TypeError:
            print("del_button 参数只能为数字")

    def set_btn_orientation(self, btn_orientation=0):
        """按钮显示方式
        """
        if btn_orientation == 0 or btn_orientation == 1:
            self.btn_orientation = btn_orientation
        else:
            print("btn_orientation 的值只能 0 或 1")

    def set_hide_avatar(self, hide_avatar=0):
        """发送者头像显示方式
        """
        if hide_avatar == 0 or hide_avatar == 1:
            self.hide_avatar = hide_avatar
        else:
            print("hide_avatar 的值只能 0 或 1")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        data = {}
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            if len(self.btns) == 1:
                data = {'msgtype': self._msgtype, 'actionCard': {
                    'text': self.content, 'title': self.title, 'hideAvatar': self.hide_avatar,
                    'btnOrientation': self.btn_orientation, 'singleTitle': self.btns[0]['title'],
                    'singleURL': self.btns[0]['actionURL']}
                }
            elif len(self.btns) > 1:
                data = {'msgtype': self._msgtype, 'actionCard': {
                    'text': self.content, 'title': self.title, 'hideAvatar': self.hide_avatar,
                    'btnOrientation': self.btn_orientation, 'btns': self.btns,
                    }
                }
            else:
                sys.exit("按钮不能为空")
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    ac = ActionCardMsg(
        "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
        "![screenshot](@lADOpwk3K80C0M0FoA)")
    ac.add_content("### 乔布斯 20 年前想打造的苹果咖啡厅")
    ac.add_button("1","3")
    # ac.del_button("v")
    print(ac.conversion_json())
