class Base(object):
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        """修改消息内容

        Args: 
            content: 消息内容(String)
        """
        self._content = content

