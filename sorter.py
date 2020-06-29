#!/usr/bin/env python3
import os
import sys
from glob import glob

FILETYPES = {
    "Documents": ("*.pdf","*.epub","*.mobi"),
    "Music": ("*.mp3","*.ogg","*.wav"),
    "Pictures": ("*.jpeg","*.jpg","*.png"),
    "Videos": ("*.mp4","*.mkv"),
    "Archives": ("*.zip", "*.tar", "*.gzip", "*.7z")
}

def mkdirs():
    subdirs = next(os.walk("."))[1]
    for key in FILETYPES.keys():
        if key not in subdirs:
            os.mkdir(key)
        else:
            pass
    return None

def movefiles():
    for ftype in FILETYPES:
        for fformat in FILETYPES[ftype]:
            filelist = glob(fformat)
            for f in filelist:
                os.rename(f, ftype+"/"+f)
    return None

def main():
    if len(os.listdir(".")) == 0:
        #print("Empty Directory. Exiting")
        return 1
    mkdirs()
    movefiles()
    return 0

if __name__ == '__main__':
    s = main()
    sys.exit(s)
