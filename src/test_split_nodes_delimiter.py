import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestTextNodeDelimiter(unittest.TestCase):
    def test_one(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, expected_nodes)

    def test_two(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.PLAIN),
        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, expected_nodes)

    def test_three(self):
        node = TextNode("This is text with a **bold word", TextType.PLAIN)
        with self.assertRaises(ValueError) as context:
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == '__main__':
    unittest.main()
