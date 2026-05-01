import re
from textnode import TextType, TextNode


def split_nodes_bold(old_nodes: list[TextNode]):
    pattern = r'\*\*(?P<bold>.*)\*\*' 
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        string = node.text
        previous_end = 0
        for m in re.finditer(pattern, string):
            if m.start() > previous_end:
                new_nodes.append(TextNode(string[previous_end:m.start()], TextType.PLAIN))
            new_nodes.append(TextNode(m.group('bold'), TextType.BOLD))
            previous_end = m.end()
        if previous_end < len(string):
            new_nodes.append(TextNode(string[previous_end:], TextType.PLAIN))
    return new_nodes


if __name__ == '__main__':
    string = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)'
    result = split_nodes_bold([TextNode(string, TextType.PLAIN)])
    for r in result:
        print(r)