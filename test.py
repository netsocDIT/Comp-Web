#!/usr/bin/python3
import glob
import os

def webp(directory, quality):
    imgs = glob.glob("img/*")
    for img in imgs:
        print(img)

        cmd = ("cwebp -q " + str(quality) + " " + img + " -o " + img[:img.index(".")-1] + ".webp")
        print(cmd)
        os.system(cmd)

webp("img/*.jpg",80)
