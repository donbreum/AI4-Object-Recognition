#!/usr/bin/env python
import xml.etree.ElementTree as ET
import glob
from pathlib import Path
import os

# scale all image digits down with this factor
SCALE_FACTOR = 8

if __name__ == "__main__":

    path = os.path.dirname(os.path.abspath(__file__))

    xml_folder = path + '/source_image_annotation/27092018_pallet_moving_L_annotations/'
    xml_folder_new = path + '/source_image_annotation/27092018_pallet_moving_L_annotations_scaled_darkflow/'

    for filepath in glob.iglob(xml_folder + '*.xml'):
        filename = filepath.split('/')[-1]

        tree = ET.parse(xml_folder + filename)  
        root = tree.getroot()

        for elem in root.iter('width'): 
            elem.text = str(int(elem.text)/SCALE_FACTOR)

        for elem in root.iter('height'): 
            elem.text = str(int(elem.text)/SCALE_FACTOR)

        for elem in root.iter('xmin'): 
            elem.text = str(int(elem.text)/SCALE_FACTOR)

        for elem in root.iter('ymin'): 
            elem.text = str(int(elem.text)/SCALE_FACTOR)

        for elem in root.iter('xmax'): 
            elem.text = str(int(elem.text)/SCALE_FACTOR)

        for elem in root.iter('ymax'): 
            elem.text = str(int(elem.text)/SCALE_FACTOR)

        tree.write(xml_folder_new + filename)  