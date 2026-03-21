import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_2_grandchildren_2_children(self):
        grandchild_node1 = LeafNode("b", "bold")
        grandchild_node2 = LeafNode("i", "italics")
        child_node1 = LeafNode("h3", "heading level 3")
        child_node2 = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><h3>heading level 3</h3><span><b>bold</b><i>italics</i></span></div>",
        )

    def test_repr(self):
        child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node])
        expected = "ParentNode(div, [LeafNode(a, Click me!, {'href': 'https://www.google.com'})], None)"
        self.assertEqual(repr(parent_node), expected)


if __name__ == "__main__":
    unittest.main()
