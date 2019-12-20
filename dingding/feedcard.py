"""FeedCard 类型
"""
import json


class FeedCardMsg(object):
    __msgtype = "feedCard"

    def __init__(self, links=[]):
        """初始化

        :param links: 消息链接
        """
        self._links = []
        for link in links:
            if len(link) == 3:
                new_link = {
                    'title': link[0], 'messageURL': link[1], 'picURL': link[2]
                }
                self._links.append(new_link)
            else:
                raise ValueError("标题或 URL 不能为空")

    @property
    def link(self):
        return self._links

    @link.setter
    def link(self, links):
        """修改链接
        """
        self._links.clear()
        for link in links:
            if len(link) == 3:
                new_link = {
                    'title': link[0], 'messageURL': link[1], 'picURL': link[2]
                }
                self._links.append(new_link)
            else:
                raise ValueError("标题或 URL 不能为空")

    def conversion_json(self):
        """转换内容为 JSON 格式
        """
        if len(self._links) < 1:
            raise ValueError("消息 URL 不能为空")
        else:
            data = {'msgtype': self.__msgtype, 'feedCard': {
                'links': self._links}
            }
            return json.dumps(data)


# 测试
if __name__ == '__main__':
    links = [[1, 2, 3], [4, "a"]]
    fc = FeedCardMsg(links)
    print(fc.conversion_json())

