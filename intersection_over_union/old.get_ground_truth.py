#!/usr/bin/env python3
# import cv2
# from darkflow.net.build import TFNet
import numpy as np
# import time
# import matplotlib.pyplot as plt
# import cv2
import sys
import os
import glob

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

def load_annotations(annotation_folder, start, end, image_h, image_w):
    run = False
    for infile in sorted(glob.glob(annotation_folder+"*.txt")):
        file_name = os.path.basename(infile)
        if file_name == start:
            run = True
        # if we want the last file included have run here, else
        # have run after next if statement
        if run:
            # print(file_name)
            box = open(infile).readline().split()[1:]
            for i in range(len(box)):
                box[i] = float(box[i])
            box = np.asarray(box)
            # import pdb;pdb.set_trace()
            print(file_name)
            convert_from_relative_to_abs(image_h, image_w, box)
        if file_name == end: 
            run = False


    print("finish load annotation")

def convert_from_relative_to_abs(image_h, image_w, box):
    box[0] = box[0] * image_h
    box[1] = box[1] * image_w
    box[2] = box[0] + box[2] * image_h
    box[3] = box[1] + box[3] * image_w

    # import pdb;pdb.set_trace()
    print(box)

def run(image_w, image_h):
    a_path, start_file, end_file = init()
    load_annotations(a_path, start_file, end_file, image_h, image_w)



if __name__=='__main__':
    run(324,256)
