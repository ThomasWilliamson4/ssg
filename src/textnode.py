from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            new_leaf = LeafNode(None, text_node.text)
                
        case TextType.BOLD:
                new_leaf = LeafNode("b",text_node.text)

        case TextType.ITALIC:
            new_leaf = LeafNode("i", text_node.text)
                
        case TextType.CODE:
            new_leaf =  LeafNode("code", text_node.text)

        case TextType.LINK:
             new_leaf =  LeafNode("a", text_node.text, {"href" : text_node.url})

        case TextType.IMAGE:
            new_leaf = LeafNode(tag ="img", value = "", props ={"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception("no text type") 

    return new_leaf   


    
    
