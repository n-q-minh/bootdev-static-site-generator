import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        node = LeafNode("p", "content", props={'property_key': 'property_value'})
        props_string = ' property_key="property_value"'
        self.assertEqual(
            str(node), 
            f'LeafNode(tag=p, value=content, props={props_string})'
        )


    def test_tag_type(self):
        node = LeafNode("a", "content", props={'href': 'some_link'})
        props_string = ' href="some_link"'
        self.assertEqual(
            str(node), 
            f'LeafNode(tag=a, value=content, props={props_string})'
        )


if __name__ == "__main__":
    unittest.main()
