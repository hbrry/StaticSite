import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="This is a text node", children=None, props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="p", value="This is a text node", children=None, props={"href": "https://www.google.com"})
        print(type(node.__dict__))  # This should print <class 'dict'>
        print(node.__dict__)        # This should print the dictionary of attributes
        self.assertDictEqual(node.__dict__, node2.__dict__)
    def test_eq_props_HTML(self):
        node = HTMLNode(props = {"href":"https://www.boot.dev","target":"_blank"})
        node2 = HTMLNode(props = {"href":"https://www.boot.dev","target":"_blank"})   
        self.assertEqual(node.props_to_html(),node2.props_to_html())
    def test_eq_value(self):
        node = HTMLNode(value = "This is a text node")
        node2 = HTMLNode(value = "This is a text node")
        self.assertEqual(node.value,node2.value)   
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()