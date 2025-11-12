import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # Test conversion of props dictionary to HTML attributes string.
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "This is a div in a simple HTMLNode",
            None,
            {"class": "website", "href": "http://example.com"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="website" href="http://example.com"',
        )
        self.assertNotEqual(
            node.props_to_html(),
            'class="website" href="http://example.com" id="test"',
        )


    # test initialization and values of HTMLNode.    
    def test_values(self):
        node = HTMLNode(
            "div",
            "Journey to Senior Software Engineer",
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Journey to Senior Software Engineer")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

        self.assertNotEqual(node.tag, "span")
        self.assertNotEqual(node.value, "Journey to no where")
        self.assertNotEqual(node.children, ["href='http://example.com'"])
        self.assertNotEqual(node.props, {"class": "website"})


    # Test the __repr__ method of HTMLNode.    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            ["This is a child node"],
            {"class": "text"}   
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode('p', 'This is a paragraph', ['This is a child node'], {'class': 'text'})"
        )

        self.assertNotEqual(
            node.__repr__(),
            "HTMLNode(div, , [This is a division element], {None})"
        )
        

class TestLeafAndParentNode(unittest.TestCase):
    # Test LeafNode functionality.
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_span(self):
        node = LeafNode("span", "This is a span element")
        self.assertEqual(node.to_html(), "<span>This is a span element</span>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a text node without a tag")
        self.assertEqual(node.to_html(), "This is a text node without a tag")
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "This is a link", {"href": "http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">This is a link</a>')
    
    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("div", None)
            node.to_html()
    

    # test ParentNode functionality.
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None, [])
            parent_node.to_html()
    
    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", [])
            parent_node.to_html()
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()