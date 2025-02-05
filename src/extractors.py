from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output_nodes = [] # a list of nodes
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_nodes.append(node)
            continue
        
        split_node = node.text.split(delimiter)
        # we use a modulo to find the remainder of dividing the length by 2 because the len should always be odd (original string + 2 delim strings)
        #end case first to avoid nesting
        split_output = []
        if len(split_node) % 2 == 0:
            raise ValueError("Markdown opened but not closed in input")
        for i in range (len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0: # even cases where text type will be text
                split_output.append(TextNode(split_node[i], TextType.NORMAL))
            else:
                split_output.append(TextNode(split_node[i], text_type))
        output_nodes.extend(split_output)  #extend by iterable list
    return output_nodes
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)" , text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
            
def split_nodes_image(old_nodes):
    output_nodes =[]
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            output_nodes.append(node)
            continue
        for image in images:
            #here
            

def split_nodes_link(old_nodes):
    output_nodes =[]
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_nodes.append(node)
            continue
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            output_nodes.append(node)
            continue
        for link in links:
            #here