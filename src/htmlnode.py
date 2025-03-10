class HTMLNode:
    def __init__(self,tag = None,value = None,children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        return (f" href={self.props["href"]} target={self.props["target"]}")
    def __repr__(self):
        return print (f"HTMLNode({self.text},{self.value},{self.children},{self.props})")
    
class LeafNode(HTMLNode):
    def __init__(self,tag ,value, props = None):
        super().__init__(tag,value,props)
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props = None):
        super().__init__(tag,children,props)
    def to_html(self):