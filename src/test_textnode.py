import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
    
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_empty_string(self):
        node = TextNode("", TextType.IMAGE)
        node2 = TextNode("", TextType.IMAGE)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, normal, https://www.boot.dev)", repr(node))


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()