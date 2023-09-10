import os

folder_path = "C:\\Data\\Buckeye Vertical\\Prelim Detection Dataset\\test\\labels" # replace with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".png.txt"):
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, filename[:-8] + ".txt"))
