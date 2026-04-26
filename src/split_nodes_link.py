import re
from textnode import TextType, TextNode


def split_nodes_link(old_nodes: list[TextNode]):
    pattern = r'(?P<plain_text>.*?)(?<!!)\[(?P<link_text>[^\(]*)\]\((?P<link_url>[^\[]*)\)'
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        matches = re.finditer(pattern, node.text)
        for m in matches:
            new_nodes.append(TextNode(m.group('plain_text'), TextType.PLAIN))
            new_nodes.append(TextNode(m.group('link_text'), TextType.LINK, m.group('link_url')))
    return new_nodes