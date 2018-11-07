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

class AllAnnotations():
    def __init__(self):
        self.files = np.array([],dtype=np.ndarray)

class AnnotationFile():
    def __init__(self, name):
        self.file_name = name
        self.boxes = np.array([],dtype=np.ndarray)

class Box():
    def __init__(self):
        self.xmin = np.asarray([],dtype=np.int32)
        self.ymin = np.asarray([],dtype=np.int32)
        self.xmax = np.asarray([],dtype=np.int32)
        self.ymax = np.asarray([],dtype=np.int32)

def init(a_path, st_path, ef_path):
    annotation_path = a_path
    start_file_path = st_path
    end_file_path = ef_path
    start_file = os.path.basename(start_file_path)
    end_file = os.path.basename(end_file_path)
    # print("Annotation folder path: {0}".format(annotation_path))
    # print("Start file path: {0}".format(start_file))
    # print("End file path: {0}".format(end_file))
    return annotation_path, start_file, end_file

def load_annotations(annotation_folder, start, end, file_collection):
    boxes = np.array(["",0,0,0,0],dtype=np.ndarray)
    # files = np.array([],dtype=np.ndarray)
    
    for infile in sorted(glob.glob(annotation_folder+ '*.xml')):
        file_name = os.path.basename(infile)
        
        annotation_file = AnnotationFile(file_name)
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
                box = Box()
                box.xmin = int(boxes_file_t[i][1])
                box.ymin = int(boxes_file_t[i][2])
                box.xmax = int(boxes_file_t[i][3])
                box.ymax = int(boxes_file_t[i][4])   
                annotation_file.boxes = np.append(annotation_file.boxes,box)
            file_collection.files = np.append(file_collection.files, annotation_file)
            # print("files append")
        else:
            print("No annotations found in %s" % file_name)
        
    # import pdb; pdb.set_trace()
    boxes = boxes[1:]
    # print (boxes)
    
    # print("finish load annotations")

def run_get_ground_truth(annotation_path, start_file_path, end_file_path):
    file_collection = AllAnnotations()
    a_path, start_file, end_file = init(annotation_path, start_file_path, end_file_path)
    load_annotations(a_path, start_file, end_file, file_collection)
    return file_collection

if __name__=='__main__':
    pass
    # run_get_ground_truth()
