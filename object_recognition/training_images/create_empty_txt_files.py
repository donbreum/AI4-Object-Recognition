#!/usr/bin/env python3

import glob
from pathlib import Path
import os
import sys

def create_empty_txt(txt_folder):
    print(txt_folder)
    for infile in sorted(glob.glob(txt_folder+ '*.jpg')):
        file_name = os.path.basename(infile)[:-4] + '.txt'
        with open(file_name, 'w') as fi:
            fi.write('') 

        print(file_name)
        pass

    return None


if __name__=='__main__':
    txt_path = sys.argv[1]
    create_empty_txt(txt_path)