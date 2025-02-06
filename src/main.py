from copystatic import copy_source_to_dest

source_dir = "./static"
dest_dir = "./public"



def main():
    copy_source_to_dest(source_dir, dest_dir)
    

if __name__ == "__main__":
    main()    