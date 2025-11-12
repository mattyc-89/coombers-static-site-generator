class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children:list=None, props:dict=None):
        # Initialize an HTMLNode with a tag, value, children, and properties.
        self.tag: str = tag
        self.value: str = value
        self.children: list = children
        self.props: dict = props
 
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method") 
    
    def props_to_html(self):
    # Convert props dictionary to HTML attributes string. It will add a space if there are props.
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html     

    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})"
    
 
class LeafNode(HTMLNode):
# A LeafNode is a simple HTMLNode that does not have children.
    def __init__(self, tag: str, value: str, props: dict=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None for LeafNode")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag!r}, {self.value!r}, {self.props!r})"
    

class ParentNode(HTMLNode):
    # A ParentNode is an HTMLNode that can have children.
    def __init__(self, tag: str, children:list, props: dict=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        