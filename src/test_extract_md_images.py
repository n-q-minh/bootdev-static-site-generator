import unittest
from extract_by_pattern import extract_markdown_images


class TestExtractMDImages(unittest.TestCase):
    def test_one(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expectation = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)
        self.assertEqual(expectation, result)

if __name__ == '__main__':
    unittest.main()