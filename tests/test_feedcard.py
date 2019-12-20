import sys; sys.path.append("..")
import unittest

from dingding.feedcard import FeedCardMsg


class TestText(unittest.TestCase):
    def test_init(self):
        link = [[1, 2, 3], [4, "a"]]
        with self.assertRaises(ValueError):
            fc = FeedCardMsg(link)
        link = [[1, 2, 3], [4]]
        with self.assertRaises(ValueError):
            fc = FeedCardMsg(link)

    def test_link(self):
        fc = FeedCardMsg([])
        link = [[1, 2, 3], [4]]
        with self.assertRaises(ValueError):
            fc.link = link

    def test_conversion_json(self):
        fc = FeedCardMsg([])
        with self.assertRaises(ValueError):
            fc.conversion_json()


if __name__ == "__main__":
    unittest.main()
