import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_1_node_1_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_1_node_2_code_blocks(self):
        node = TextNode(
            "This is text with 2 code blocks: `code block 1` and `code block 2`",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with 2 code blocks: ", TextType.TEXT),
                TextNode("code block 1", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("code block 2", TextType.CODE),
            ],
        )

    def test_1_node_1_starting_code_block(self):
        node = TextNode(
            "`Code block` at the beginning",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Code block", TextType.CODE),
                TextNode(" at the beginning", TextType.TEXT),
            ],
        )

    def test_1_node_1_ending_code_block(self):
        node = TextNode(
            "This ends with a `code block`",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This ends with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
        )

    def test_2_text_nodes_3_bolds_1_link_node_1_image_node(self):
        text_node1 = TextNode("Go to **Google**", TextType.TEXT)
        text_node2 = TextNode("This is an **image** of a **dog**", TextType.TEXT)
        link_node = TextNode(
            "Go to **Google**", TextType.LINK, "https://www.google.com"
        )
        image_node = TextNode(
            "This is an **image** of a **dog**",
            TextType.IMAGE,
            "https://repository.com/dog.jpg",
        )
        new_nodes = split_nodes_delimiter(
            [text_node1, text_node2, link_node, image_node], "**", TextType.BOLD
        )
        self.assertEqual(
            new_nodes,
            [
                TextNode("Go to ", TextType.TEXT),
                TextNode("Google", TextType.BOLD),
                TextNode("This is an ", TextType.TEXT),
                TextNode("image", TextType.BOLD),
                TextNode(" of a ", TextType.TEXT),
                TextNode("dog", TextType.BOLD),
                TextNode("Go to **Google**", TextType.LINK, "https://www.google.com"),
                TextNode(
                    "This is an **image** of a **dog**",
                    TextType.IMAGE,
                    "https://repository.com/dog.jpg",
                ),
            ],
        )

    def test_1_bold_node_should_skip_delimiter(self):
        node = TextNode("This `bold` node has to skip the delimiter!", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This `bold` node has to skip the delimiter!", TextType.BOLD),
            ],
        )

    def test_1_node_1_code_block_missing_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)

        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            str(cm.exception),
            "Invalid Markdown syntax: It's missing a closing delimiter!",
        )
