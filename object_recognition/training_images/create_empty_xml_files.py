#!/usr/bin/env python3

import glob
from pathlib import Path
import os
import sys

def create_empty_xml(path):
    # print(txt_folder)
    for infile in sorted(glob.glob(path+ '*.jpg')):
        file_name_jpg = os.path.basename(infile)
        file_name_xml = os.path.basename(infile)[:-4] + '.xml'
        with open(file_name_xml, 'w') as fi:
            fi.write ("<?xml version=""1.0""?>\n"
                        "<annotation>\n"
                        "<folder>data</folder>\n"
                        "<filename>" + file_name_jpg + "</filename>\n"
                        "<path/>\n"
                        "<source>\n"
                        "<database>Unknown</database>\n"
                        "</source>\n"
                        "<size>\n"
                        "<width>480</width>\n"
                        "<height>270</height>\n"
                        "<depth>3</depth>\n"
                        "</size>\n"
                        "<segmented>0</segmented>\n"
                        "</annotation>")
    return None

if __name__=='__main__':
    path = sys.argv[1]
    create_empty_xml(path)