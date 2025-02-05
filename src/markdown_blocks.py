import re
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node
from extractors import text_to_textnodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
 
    return stripped_blocks

def block_to_block_type(block):
    if re.match(r'^#{1,6}\s+\w', block):
        return "heading"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return "quote"
    if all(line.startswith(("* ","- ")) for line in lines):
        return "unordered list"
    for i in range(len(lines)):
        number = f"{i + 1}. "
        if not lines[i].startswith(number):
            break
    else: 
        return "ordered list"
   
    return "paragraph"

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        html = text_node_to_html_node(node)
        children.append(html)
    return children

def convert_paragraph_block(block):
    stripped_text = block.strip()
    children = text_to_children(stripped_text)
    return ParentNode("p", children)

def convert_heading_block(block):
    head = 0
    for char in block:
        if char == "#":
            head +=1
        else:
            break
    if head == 0 or head>6:
        raise ValueError(f"invalid heading {head}")
    text = block[head:]
    stripped_text = text.strip()
    children = text_to_children(stripped_text)
    return ParentNode(f"h{head}", children)
    

def convert_code_block(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code")
    stripped_text = block.lstrip("```").rstrip("```").strip()
    children = text_to_children(stripped_text)
    code = ParentNode("code", children)
    return ParentNode("pre", code)


def convert_quote_block(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quotes")
        stripped_lines.append(line.lstrip(">").strip())
    stripped_text = "\n".join(stripped_lines)
    children = text_to_children(stripped_text)
    return ParentNode("blockquote", children)


def convert_unordered_list_block(block):
    lines = block.split("\n")
    html = []
    for line in lines:





    
    return ParentNode("ul", unordered)

def convert_ordered_list_block(block):






    
    return ParentNode("ol", ordered)









def block_to_html(block):
    type = block_to_block_type(block)
    if type == "code":
        return convert_code_block(block)
    if type == "quote":
        return convert_quote_block(block)
    if type == "unordered list":
        return convert_unordered_list_block(block)
    if type == "ordered list":
        return convert_ordered_list_block(block)
    if type == "heading":
        return convert_heading_block(block)
    if type == "paragraph":
        return convert_paragraph_block(block)
    raise ValueError("invalid block type")

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    #blocks to children
    return ParentNode("div", children)
  

        



        

