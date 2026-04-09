import unittest

from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links_beginning_middle(self):
        node = TextNode(
            "[Go to Google](https://google.com) and middle link [ABC link](https://abc.com) that's all!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Go to Google", TextType.LINK, "https://google.com"),
                TextNode(" and middle link ", TextType.TEXT),
                TextNode("ABC link", TextType.LINK, "https://abc.com"),
                TextNode(" that's all!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_middle_end(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode(
            "This is a text with no links whatsoever! So it should be returned as is!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is a text with no links whatsoever! So it should be returned as is!",
                    TextType.TEXT,
                )
            ],
            new_nodes,
        )

    def test_various_nodes(self):
        node_1 = TextNode(
            "[Go to Google](https://google.com) and middle link [ABC link](https://abc.com) that's all!",
            TextType.TEXT,
        )
        node_2 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node_3 = TextNode(
            "This is a text with no links whatsoever! So it should be returned as is!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node_1, node_2, node_3])
        self.assertListEqual(
            [
                TextNode("Go to Google", TextType.LINK, "https://google.com"),
                TextNode(" and middle link ", TextType.TEXT),
                TextNode("ABC link", TextType.LINK, "https://abc.com"),
                TextNode(" that's all!", TextType.TEXT),
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(
                    "This is a text with no links whatsoever! So it should be returned as is!",
                    TextType.TEXT,
                ),
            ],
            new_nodes,
        )
