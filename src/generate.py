from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise ValueError("no heading") 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    page_nodes = markdown_to_html_node(markdown)
    page_html = page_nodes.to_html()
    title = extract_title(markdown)

    template.replace("{{TITLE}}", title)
    template.replace("{{CONTENT}}", page_html)
    

