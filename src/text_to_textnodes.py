from split_nodes_bold import split_nodes_bold
from split_nodes_italic import split_nodes_italic
from split_nodes_code import split_nodes_code
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextType, TextNode

def text_to_textnodes(text):
    node = TextNode(text, TextType.PLAIN)
    nodes = [node]

    split_bold = split_nodes_bold(nodes)
    split_italic = split_nodes_italic(split_bold)
    split_code = split_nodes_code(split_italic)
    split_image = split_nodes_image(split_code)
    split_link = split_nodes_link(split_image)
    return split_link


if __name__ == '__main__':
    string = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    result = text_to_textnodes(string)
    for r in result:
        print(r)