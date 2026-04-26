from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Leaf node has no value')
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        props_string = self.props_to_html()
        return f'LeafNode(tag={self.tag}, value={self.value}, props={props_string})'
    