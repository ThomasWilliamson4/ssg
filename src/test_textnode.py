import unittest

from textnode import TextNode, TextType


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

    def test_text_to_node(self):
        node = TextNode("This is a link node", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(node.text_node_to_html_node(),'<img src="https://www.boot.dev" alt="This is a link node"></img>')




if __name__ == "__main__":
    unittest.main()