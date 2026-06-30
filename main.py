import os
import shutil

# Current absolute path
CURRENT__DIR = os.path.dirname(os.path.abspath(__file__)) 

# The target folder
TARGET_DIR = CURRENT__DIR

# The program main.py
MAIN = os.path.basename(__file__)

EXTENSION_MAP = {
    '.jpg': '圖片',
    '.jpeg': '圖片',
    '.png': '圖片',
    '.gif': '圖片',
    '.txt': '文件',
    '.pdf': '文件',
    '.docx': '文件',
    '.pptx': '簡報',
    '.mp3': '音樂',
    '.mp4': '音樂',
    '.zip': '壓縮包',
    '.exe': '安裝檔' 
}

def scan_and_move():

    print(f"📍 Detected current directory: {TARGET_DIR}")
    print(f"🚀 Start organizing...\n")
    
    #Check the path whether exist
    if not os.path.exists(TARGET_DIR):
        print(f"{TARGET_DIR} is not exist, please build it first\n")
        return

    #Read all item in target folder
    all_items = os.listdir(TARGET_DIR)

    #Check all items one by one
    for item in all_items:

        # We cannot move main.py 
        if item == MAIN:
            continue
         
        full_path = os.path.join(TARGET_DIR, item)

        # If item is folder just skip(we will just solve file)
        if os.path.isdir(full_path):
            continue
        
        # Split the item
        name, ext = os.path.splitext(item)

        # Ex: jpg, JPG is same
        ext = ext.lower()
        
        if ext in EXTENSION_MAP:

            folder_name = EXTENSION_MAP[ext]
            dest_folder = os.path.join(TARGET_DIR, folder_name)
            
            # If the folder is not exists, build a new folder
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                print(f"📁 Build a new folder: {folder_name} !\n")

            # The destination path of the file
            dest_file_path = os.path.join(dest_folder, item)

            # Move the file
            shutil.move(full_path, dest_file_path)
            print(f"🚚 {item} -> move to {folder_name}\n")
        
        else:
            print(f"{item} will at same position\n")
    
    print("Stop scanning, organization completed!\n")

if __name__ == '__main__':
    scan_and_move()