"""ActionCard 类型
"""
import json


class ActionCardMsg(object):
    def __init__(
            self, title, content, single_title, single_url,
            btn_orientation=1, hide_avatar=0):
        """
        初始化

        :param title: 标题 
        :param content: 消息内容（Markdown 格式）
        :param single_title: 按钮名称
        :param single_url: 按钮跳转 URL
        :param btn_orientation: 0-1-按钮横向排列
        :param hide_avatar: 0-正常发消息者头像，1-隐藏发消息者头像
        """
        self._msgtype = "actionCard"
        self.title = title
        self.content = content
        self.single_title = single_title
        self.single_url = single_url
        self.btn_orientation = btn_orientation
        self.hide_avatar = hide_avatar

    def mod_title(self, title):
        """
        修改标题
        """
        if not title.strip():
            self.title = title
        else:
            print("title 不能为空")

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

    def mod_single_title(self, single_title):
        """
        修改按钮标题
        """
        if not single_title.strip():
            self.single_title = single_title
        else:
            print("single_title 不能为空")

    def mod_single_url(self, single_url):
        """
        修改跳转 URL
        """
        if not single_url.strip():
            self.single_url = single_url
        else:
            print("single_url 不能为空")

    def set_btn_orientation(self, btn_orientation=1):
        """
        按钮显示方式
        """
        if btn_orientation == 0 or btn_orientation == 1:
            self.btn_orientation = btn_orientation
        else:
            sys.exit("btn_orientation 的值只能 0 或 1")

    def set_hide_avatar(self, hide_avatar=0):
        """
        发送者头像显示方式
        """
        if hide_avatar == 0 or hide_avatar == 1:
            self.hide_avatar = hide_avatar
        else:
            sys.exit("hide_avatar 的值只能 0 或 1")

    def conversion_json(self):
        """
        转换内容为 JSON 格式
        """
        if len(self.content) == 0:
            sys.exit("内容不能为空")
        else:
            data = {'msgtype': self._msgtype, 'actionCard': {
                'text': self.content, 'title': self.title, 'hideAvatar': self.hide_avatar,
                'btnOrientation': self.btn_orientation, 'singleTitle': self.single_title,
                'singleURL': self.single_url}
            }
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    ac = ActionCardMsg(
        "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
        "![screenshot](@lADOpwk3K80C0M0FoA)",
        "阅读全文","https://www.dingtalk.com/")
    ac.add_content("### 乔布斯 20 年前想打造的苹果咖啡厅")
    # ac.del_content()
    ac.set_btn_orientation(0)
    # ac.set_hide_avatar(1)
    print(ac.conversion_json())
