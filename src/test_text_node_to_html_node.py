import unittest

from leafnode import LeafNode
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text")

    def test_italic(self):
        node = TextNode("This is a italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text")

    def test_code(self):
        node = TextNode("This is a code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code")

    def test_link(self):
        node = TextNode("Go to Google", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Go to Google")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_img(self):
        node = TextNode(
            "This is an image of a dog",
            TextType.IMAGE,
            "https://repository.com/dog.jpg",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                "src": "https://repository.com/dog.jpg",
                "alt": "This is an image of a dog",
            },
        )
