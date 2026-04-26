import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_one(self):
        node = HTMLNode()
        self.assertTrue(node.tag == None)

    def test_two(self):
        node = HTMLNode(
            tag='a', 
            value='some text', 
            children=None, 
            props={'href': 'www.crz.sk', 'label': 'central'}
        )
        self.assertEqual(node.props_to_html(), ' href="www.crz.sk" label="central"')

    def test_three(self):
        node = HTMLNode(
            tag='a', 
            value='some text', 
            children=None, 
            props=None
        )
        self.assertEqual(node.props_to_html(), '')

    def test_four(self):
        node = HTMLNode(
            tag='p', 
            value='lorem ipsum', 
            children=[HTMLNode(), HTMLNode()], 
            props=None
        )
        self.assertEqual(len(node.children), 2)


if __name__ == "__main__":
    unittest.main()