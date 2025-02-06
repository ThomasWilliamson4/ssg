import os
import shutil

def copy_source_to_dest(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    filepath = os.listdir(source)
    for file in filepath:
        source_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)
        if os.path.isdir(source_path):
            print(f"mkdir{dest_path}")
            copy_source_to_dest(source_path,dest_path)
        else:
            shutil.copy(source_path, dest_path)
            print(f"copying file{dest_path}")
