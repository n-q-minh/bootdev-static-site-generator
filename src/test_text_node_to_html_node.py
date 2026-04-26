import unittest
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node


class TestTextNodeConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode(text="This is a text node", text_type=TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_url(self):
        node = TextNode(
            text='This is a link node', 
            text_type=TextType.LINK,
            url='www.boot.dev'
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'This is a link node')
        self.assertEqual(html_node.props, {'href': 'www.boot.dev'})

    def test_unrecognised_type(self):
        node = TextNode(text='This is a text node', text_type='abc')
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)


if __name__ == '__main__':
    unittest.main()