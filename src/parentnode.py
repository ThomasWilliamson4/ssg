from htmlnode import HTMLNode

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
