import sys; sys.path.append("..")
import unittest

from dingding.link import LinkMsg


class TestText(unittest.TestCase):
    def test_title(self):
        link = LinkMsg("title", "content", "msg")
        link.title = "t"
        self.assertEqual(link.title, "t")

    def test_mod_msg_url(self):
        link = LinkMsg("title", "content", "msg")
        with self.assertRaises(ValueError):
            link.mod_msg_url("")

    def test_conversion_json(self):
        link = LinkMsg("", "content", "msg")
        with self.assertRaises(ValueError):
            link.conversion_json()
        link = LinkMsg("title", "", "msg")
        with self.assertRaises(ValueError):
            link.conversion_json()
        link = LinkMsg("title", "content", "")
        with self.assertRaises(ValueError):
            link.conversion_json()


if __name__ == "__main__":
    unittest.main()
