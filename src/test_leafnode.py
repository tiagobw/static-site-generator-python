import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h3(self):
        node = LeafNode("h3", "This is a heading level 3!")
        self.assertEqual(node.to_html(), "<h3>This is a heading level 3!</h3>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
