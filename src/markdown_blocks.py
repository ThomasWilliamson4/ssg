import re
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node


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


def convert_paragraph_block(text):

def convert_heading_block(text):

def convert_code_block(text):

def convert_quote_block(text):

def convert_unordered_list_block(text):

def convert_ordered_list_block(text):




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
  

        



        

