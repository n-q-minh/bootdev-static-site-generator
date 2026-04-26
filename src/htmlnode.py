class HTMLNode:
    def __init__(
            self, 
            tag: str = None, 
            value: str = None, 
            children: list = None, 
            props: dict[str, str] = None
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ''
        if self.props == dict():
            return ''
        strings = []
        for key, value in self.props.items():
            string = f' {key}="{value}"'
            strings.append(string)
        result = ''.join(strings)
        return result
    
    def __repr__(self):
        props_string = self.props_to_html()
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={props_string})'
    