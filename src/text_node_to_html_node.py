from textnode import TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):
	text_type = text_node.text_type
	if text_type not in TextType:
		raise ValueError('Unrecognised text type')
	
	props = None
	text = text_node.text
	match text_type:
		case TextType.PLAIN:
			tag = None
		case TextType.BOLD:
			tag = 'b'
		case TextType.ITALIC:
			tag = 'i'
		case TextType.CODE:
			tag = 'code'
		case TextType.LINK:
			tag = 'a'
			props = {'href': text_node.url}
		case TextType.IMAGE:
			tag = 'img'
			text = ''
			props = {'src': text_node.url, 'alt': text_node.text}
	
	return LeafNode(tag=tag, value=text, props=props)