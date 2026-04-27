import re
from textnode import TextType, TextNode


def split_nodes_image(old_nodes: list[TextNode]):
    pattern = r'(?P<plain_text>.*?)!\[(?P<image_text>[^\(]*)\]\((?P<image_url>[^\[]*)\)'
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        matches = re.finditer(pattern, node.text)
        for m in matches:
            new_nodes.append(TextNode(m.group('plain_text'), TextType.PLAIN))
            new_nodes.append(TextNode(m.group('image_text'), TextType.IMAGE, m.group('image_url')))
    return new_nodes


if __name__ == '__main__':
    pattern = r'!\[(?P<image_text>[^\(]*)\]\((?P<image_url>[^\[]*)\)'
    string = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    
    result = []
    previous_end = 0

    for m in re.finditer(pattern, string):
        if m.start() > previous_end:
            result.append(TextNode(string[previous_end:m.start()], TextType.PLAIN))
            # result.append({"type": "text", "content": string[previous_end:m.start()]})
        result.append(TextNode(m.group('image_text'), TextType.IMAGE, m.group('image_url')))
        # result.append({"type": "image", **m.groupdict()})
        previous_end = m.end()
    
    if previous_end < len(string):
        result.append(TextNode(string[previous_end:], TextType.PLAIN))
        # result.append({"type": "text", "content": string[previous_end:]})

    for item in result:
        print(item)