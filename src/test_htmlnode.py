import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
    
    def test_props_to_html(self):
        node = HTMLNode()
        node.props = {"class": "container", "id": "main"}
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')
    
    def test_to_html(self):
        pass

    def test_none_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
   
    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), 'Tag: p, Value: What a strange world, Children: None, Props: class="primary"')


