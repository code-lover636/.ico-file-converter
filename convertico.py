from PIL import Image
import os,PIL
from easygui import diropenbox

FOLDER = diropenbox()
count = 0
try:
    for img in os.listdir(FOLDER):
        try:
            if not img.endswith(".ico"):
                im = Image.open(FOLDER+"/"+img)
                rgb_img = im.convert('RGBA')
                rgb_img.save(FOLDER+"\\"+img[:-4]+'.ico')
                os.remove(FOLDER+"\\"+img)
                count+=1
        except PIL.UnidentifiedImageError:
            print(img,"cannot be converted.")
    if count == 0: print("No files in this directory is convertible to .ico")
    else: print(f"CONVERSION SUCCESSFULL!\n{count} files converted")
except NotADirectoryError:
    print("Please select a directory")
