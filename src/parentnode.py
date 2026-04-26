from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('Parent node has no tag')
        if self.children is None:
            raise ValueError('Parent node has no children')
        
        parts = []
        for child in self.children:
            parts.append(child.to_html())

        return f"<{self.tag}{self.props_to_html()}>{''.join(parts)}</{self.tag}>"