import sys; sys.path.append("..")
import unittest

from dingding.markdown import MarkdownMsg


class TestText(unittest.TestCase):
    def test_title(self):
        md = MarkdownMsg("title", "test")
        md.title = "t"
        self.assertEqual(md.title, "t")

    def test_conversion_json(self):
        md = MarkdownMsg("", "test")
        with self.assertRaises(ValueError):
            md.conversion_json()
        md = MarkdownMsg("title", "")
        with self.assertRaises(ValueError):
            md.conversion_json()


if __name__ == "__main__":
    unittest.main()
