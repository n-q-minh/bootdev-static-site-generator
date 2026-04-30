import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_split_images_simple(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_split_nodes_complex(self):
        string = 'This is **text** with an _italic_ word and a `code block` and some [link](https://www.reddit.com) an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and another [link](https://boot.dev)'
        node = TextNode(string, TextType.PLAIN)
        result = split_nodes_link([node])
        expected_result = [
            TextNode('This is **text** with an _italic_ word and a `code block` and some ', TextType.PLAIN),
            TextNode('link', TextType.LINK, 'https://www.reddit.com'),
            TextNode(' an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and another ', TextType.PLAIN),
            TextNode('link', TextType.LINK, 'https://boot.dev')
        ]
        self.assertListEqual(result, expected_result)
        

if __name__ == '__main__':
    unittest.main()