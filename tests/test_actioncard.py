import sys; sys.path.append("..")
import unittest

from dingding.actioncard import ActionCardMsg


class TestText(unittest.TestCase):
    def test_title(self):
        ac = ActionCardMsg("title", "content")
        ac.title = "t"
        self.assertEqual(ac.title, "t")

    def test_btn(self):
        ac = ActionCardMsg("title", "content")
        with self.assertRaises(TypeError):
            ac.button = [1, 2]
        with self.assertRaises(ValueError):
            ac.button = [{"t":""}]  

    def test_set_btn_orientation(self):
        ac = ActionCardMsg("title", "content")
        with self.assertRaises(TypeError):
            ac.set_btn_orientation(1)
        with self.assertRaises(TypeError):
            ac.set_btn_orientation("a")

    def test_set_hide_avatar(self):
        ac = ActionCardMsg("title", "content")
        with self.assertRaises(TypeError):
            ac.set_hide_avatar(1)
        with self.assertRaises(TypeError):
            ac.set_hide_avatar("a")

    def test_conversion_json(self):
        ac = ActionCardMsg("", "content")
        with self.assertRaises(ValueError):
            ac.conversion_json()
        ac = ActionCardMsg("title", "")
        with self.assertRaises(ValueError):
            ac.conversion_json()
        ac = ActionCardMsg("title", "content", [])
        with self.assertRaises(ValueError):
            ac.conversion_json()


if __name__ == "__main__":
    unittest.main()
