
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
   
    def to_html(self):
        raise NotImplementedError
   
    def props_to_html(self):
        output = ""
        if self.props:
            for key, value in self.props.items():
                output += f' {key}="{value}"'
        return output
   
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props:{self.props_to_html()}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
           raise ValueError("Invalid HTML")
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
 
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: no tags")
        if self.children == None:
            raise ValueError("Invalid HTML: no children")
        output_html = f"<{self.tag}>"
        for child in self.children:
            output_html += child.to_html()
        output_html += f"</{self.tag}>"
        return output_html