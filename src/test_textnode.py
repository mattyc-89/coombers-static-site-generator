import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    # Test equality of TextNode instances.
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode ("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_eq_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        node2 = TextNode("This is a code node", TextType.CODE)
        self.assertEqual(node, node2)
    
    def test_eq_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a link node", TextType.LINK, "http://example.com")
        self.assertEqual(node, node2)
    
    def test_eq_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "http://example.com/image.png")
        node2 = TextNode("This is an image node", TextType.IMAGE, "http://example.com/image.png")
        self.assertEqual(node, node2)

    
    # Test inequality of TextNode instances.
    def test_noteq_link_different_url(self):
        node = TextNode("This is a link node", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a link node", TextType.LINK, "")
        self.assertNotEqual(node, node2)
    
    def test_noteq_text_different_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    # Test conversion from TextNode to HTMLNode.
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "http://example.com"})
    
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "This is an image node"})
    
    def test_invalid_type(self):
        with self.assertRaises(Exception):
            text_node_to_html_node("This is not a TextNode")
        

if __name__ == "__main__":
    unittest.main()
