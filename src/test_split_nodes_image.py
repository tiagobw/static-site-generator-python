import unittest

from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images_beginning_middle(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and middle image ![second image](https://i.imgur.com/3elNhQu.png) that's all!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and middle image ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" that's all!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_middle_end(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
            "This is a text with no images whatsoever! So it should be returned as is!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is a text with no images whatsoever! So it should be returned as is!",
                    TextType.TEXT,
                )
            ],
            new_nodes,
        )

    def test_various_nodes(self):
        node_1 = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and middle image ![second image](https://i.imgur.com/3elNhQu.png) that's all!",
            TextType.TEXT,
        )
        node_2 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node_3 = TextNode(
            "This is a text with no images whatsoever! So it should be returned as is!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node_1, node_2, node_3])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and middle image ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" that's all!", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                    "This is a text with no images whatsoever! So it should be returned as is!",
                    TextType.TEXT,
                ),
            ],
            new_nodes,
        )
