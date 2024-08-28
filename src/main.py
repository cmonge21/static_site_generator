import os
import shutil

def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)
    print(f"Creating new directory: {destination}")

    if not os.path.exists(source):
        raise Exception("Error, no source found")

    items = os.listdir(source)

    for item in items:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copying file: {source_path} -> {destination_path}")   
        elif os.path.isdir(source_path):
            copy_directory(source_path, destination_path)
            print(f"Copying directory: {source_path} -> {destination_path}")
            
        

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    static_dir = os.path.join(parent_dir, 'static')
    public_dir = os.path.join(parent_dir, 'public')
    copy_directory(static_dir, public_dir)

if __name__ == '__main__':
    main()
   
