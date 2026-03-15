import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        image_node = TextNode(
            "This is an image", TextType.IMAGE, "https://repository.com/image.jpg"
        )
        link_node = TextNode("This is a link", TextType.LINK, "https://repository.com")
        self.assertNotEqual(image_node, link_node)

    def test_url_is_none(self):
        code_node = TextNode("This is a code", TextType.CODE)
        self.assertEqual(code_node.url, None)

    def test_repr(self):
        node = TextNode(
            "I'm an image!", TextType.IMAGE, "https://repository.com/image.jpg"
        )
        expected = "TextNode(I'm an image!, image, https://repository.com/image.jpg)"
        self.assertEqual(repr(node), expected)

    def test_repr_no_url(self):
        node = TextNode("I'm a text without URL!", TextType.TEXT)
        expected = "TextNode(I'm a text without URL!, text, None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
