import unittest
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_other_types(self):
        node = TextNode(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is **text** with an _italic_ word and a `code block` and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a [link](https://boot.dev)", TextType.PLAIN)
            ],
            new_nodes
        )

    def test_split_complex_string(self):
        string = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and ![another image](https://www.boot.dev/lessons/21db95df-68e9-4f10-9c76-16142abba580) and a [link](https://boot.dev)'
        node = TextNode(string, TextType.PLAIN)
        result = split_nodes_image([node])
        expected_nodes = [
            TextNode('This is **text** with an _italic_ word and a `code block` and an ', TextType.PLAIN),
            TextNode('obi wan image', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
            TextNode(' and ', TextType.PLAIN),
            TextNode('another image', TextType.IMAGE, 'https://www.boot.dev/lessons/21db95df-68e9-4f10-9c76-16142abba580'),
            TextNode(' and a [link](https://boot.dev)', TextType.PLAIN)
        ]
        self.assertListEqual(expected_nodes, result)


if __name__ == '__main__':
    unittest.main()
    '''
    pattern = r'(?P<plain_text>.*?)!\[(?P<image_text>[^\(]*)\]\((?P<image_url>[^\[]*)\)'
    matches = re.finditer(pattern, string)
    for m in matches:
        print(m.group('plain_text'), m.group('image_text'), m.group('image_url')) 
    '''