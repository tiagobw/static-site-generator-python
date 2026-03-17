import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_with_props_to_html(self):
        node = HTMLNode(
            "a",
            "Google",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_without_props_to_html(self):
        node = HTMLNode(
            "h1",
            "Hi",
            None,
            None,
        )
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            "a",
            "Google",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        expected = "HTMLNode(a, Google, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
