from markdown_blocks import markdown_to_html_node



def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise ValueError("no heading") 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = # read mkdown from_path 
    template = #read template template_path
    page = markdown_to_html_node(markdown)
    page_html = page.to_html()
    title = extract_title(markdown)
    # replace title and content in template

