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
    output_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node.text)
        
        if len(images) == 0:
            output_nodes.append(node)
            continue
        
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: image")
            if sections[0] != "":
                output_nodes.append(TextNode(sections[0], TextType.NORMAL))
            
            output_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = sections[1]
        if node_text != "":
            output_nodes.append(TextNode(node_text, TextType.NORMAL))
    return output_nodes
        

def split_nodes_link(old_nodes):
    output_nodes =[]
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        node_text = node.text
        if len(links) == 0:
            output_nodes.append(node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: link")
            if sections[0] != "":
                output_nodes.append(TextNode(sections[0], TextType.NORMAL))
            
            output_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = sections[1]
        if node_text != "":
            output_nodes.append(TextNode(node_text, TextType.NORMAL))
    return output_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

