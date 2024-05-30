import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def copy_file(file_path, target_dir):
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
  
    shutil.copy2(file_path, target_dir)
    print(f"Copied {file_path} to {target_dir}")


def process_directory(src_dir, dest_dir, executor):
   
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
          
            file_ext = file.split('.')[-1].lower()
            target_dir = os.path.join(dest_dir, file_ext)
           
            executor.submit(copy_file, file_path, target_dir)


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python sort_files.py <source_directory> [<destination_directory>]")
        return

    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"


    with ThreadPoolExecutor(max_workers=4) as executor:
        process_directory(src_dir, dest_dir, executor)

# Запускаємо основну функцію
if __name__ == "__main__":
    main()
