#!/usr/bin/env python3
# import cv2
# from darkflow.net.build import TFNet
import numpy as np
# import time
# import matplotlib.pyplot as plt
# import cv2
import sys
import xml.etree.ElementTree as ET
import glob
from pathlib import Path
import os

class box():
    def __init__(self):
        xmin = np.asarray([],dtype=np.int32)
        ymin = np.asarray([],dtype=np.int32)
        xmax = np.asarray([],dtype=np.int32)
        ymax = np.asarray([],dtype=np.int32)

def init():
    annotation_path = sys.argv[1]
    start_file_path = sys.argv[2]
    end_file_path = sys.argv[3]
    start_file = os.path.basename(start_file_path)
    end_file = os.path.basename(end_file_path)
    print("Annotation folder path: {0}".format(annotation_path))
    print("Start file path: {0}".format(start_file))
    print("End file path: {0}".format(end_file))
    return annotation_path, start_file, end_file

def load_annotations(annotation_folder, start, end):
    boxes = np.array(["",0,0,0,0],dtype=np.ndarray)
    for infile in sorted(glob.glob(annotation_folder+ '*.xml')):
        file_name = os.path.basename(infile)
        # print(file_name)
        
        tree = ET.parse(annotation_folder + file_name)  
        root = tree.getroot()
        xmin = np.asarray([],dtype=np.int32)
        ymin = np.asarray([],dtype=np.int32)
        xmax = np.asarray([],dtype=np.int32)
        ymax = np.asarray([],dtype=np.int32)
        filename_str = np.asarray([],dtype=np.str)

        for elem in root.iter('xmin'):
            xmin = np.append(xmin, int(elem.text))
            filename_str = np.append(filename_str, file_name)
        for elem in root.iter('ymin'): 
            ymin = np.append(ymin, int(elem.text))
        for elem in root.iter('xmax'): 
            xmax = np.append(xmax, int(elem.text))
        for elem in root.iter('ymax'): 
            ymax = np.append(ymax, int(elem.text))

        if not len(xmin) == 0:
            boxes_file = np.array([filename_str, xmin,ymin,xmax,ymax])
            boxes_file_t = boxes_file.transpose()
            for i in range(len(boxes_file_t)):
                boxes = np.vstack((boxes, boxes_file_t[i]))       
        else:
            print("No annotations found in %s" % file_name)
        
    boxes = boxes[1:]
    print (boxes)
    
    print("finish load annotation")

def run():
    a_path, start_file, end_file = init()
    load_annotations(a_path, start_file, end_file)

if __name__=='__main__':
    run()
