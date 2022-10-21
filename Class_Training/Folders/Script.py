import os

root_folder = os.getcwd()

all_folders = os.listdir(root_folder)
for f in all_folders:
    if os.path.isdir(root_folder+"/"+f):
        print(f"found folder : [{f}]")