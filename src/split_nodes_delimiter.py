from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            result.append(old_node)
        if delimiter in old_node.text:
            if old_node.text.count(delimiter) % 2 != 0:
                raise ValueError(f"delimiter '{delimiter}' not found")
        
        parts = old_node.text.split(delimiter)
        for i, part in enumerate(parts, start=1):
            if i % 2 == 0:
                node = TextNode(part, text_type)
            else:
                node = TextNode(part, TextType.PLAIN)
            result.append(node)
    return result