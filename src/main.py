from textnode import TextNode, TextType


def main():
	text_node = TextNode('sample content', TextType.PLAIN_TEXT, None)
	print(text_node)

	text_node = TextNode('sample text', TextType.LINK, 'https://www.boot.dev')
	print(text_node)


if __name__ == '__main__':
	print('hello world')
	main()
