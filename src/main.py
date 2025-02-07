from copystatic import copy_source_to_dest
import os
import shutil
from generate import generate_page, generate_pages_recursive

static_dir = "./static"
public_dir = "./public"
source_dir = "./content/index.md"
temp_path = "./template.html"
index_path = "./public/index.html"
content = "./content"



def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    copy_source_to_dest(static_dir, public_dir)

    generate_pages_recursive(content, temp_path, public_dir)


if __name__ == "__main__":
    main()    