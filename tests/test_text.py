import sys; sys.path.append("..")
import unittest

from dingding.text import TextMsg


class TestText(unittest.TestCase):
    def test_init(self):
        txt = TextMsg("test", [123])
        self.assertEqual(txt.phone_num, ["123"])
        with self.assertRaises(TypeError):
            txt = TestText("test", [[123, 456], 4567], True)
        with self.assertRaises(TypeError):
            txt = TestText("test", [], 1)
        with self.assertRaises(TypeError):
            txt = TestText("test", [], "a")

    def test_content(self):
        txt = TextMsg("test")
        txt.content = "abc"
        self.assertEqual(txt.content, "abc")

    def test_phone_num(self):
        txt = TextMsg("test")
        txt.phone_num = [456, "789"]
        self.assertEqual(txt.phone_num, ["456", "789"])

    def test_set_at_all(self):
        txt = TextMsg("test")
        with self.assertRaises(TypeError):
            txt.set_at_all(1)
        with self.assertRaises(TypeError):
            txt.set_at_all("a")

    def test_conversion_json(self):
        txt = TextMsg("")
        with self.assertRaises(ValueError):
            txt.conversion_json()


if __name__ == "__main__":
    unittest.main()
