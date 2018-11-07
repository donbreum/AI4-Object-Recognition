#!/usr/bin/env python3
import cv2
# from darkflow.net.build import TFNet
import numpy as np
import os
import sys
# import time
# import matplotlib.pyplot as plt
# import cv2

# import xml.etree.ElementTree as ET
# import glob
# from pathlib import Path

class AllResults():
    def __init__(self):
        self.files = np.array([],dtype=np.ndarray)

class ResultFile():
    def __init__(self, name):
        self.file_name = name
        self.boxes = np.array([],dtype=np.ndarray)

class Box():
    def __init__(self):
        self.already_used = False
        self.xmin = np.asarray([],dtype=np.int32)
        self.ymin = np.asarray([],dtype=np.int32)
        self.xmax = np.asarray([],dtype=np.int32)
        self.ymax = np.asarray([],dtype=np.int32)

def run_get_results(result_file_path):
    result_collection = AllResults()

    # file_names = np.array([],dtype=np.str) # deprecated
    f = open(result_file_path,"r")
    results_file = f.readlines()
    for i in range(len(results_file)):
        
        if results_file[i].find("jpg") > 0:
            
            # find a line with jpg (indicate found result)
            jpg_end_idx = results_file[i].find("jpg") + 3
            file_path = results_file[i][18:jpg_end_idx]
            file_name = os.path.basename(file_path)
            # file_names = np.append(file_names,file_name) # deprecated
            # import pdb;pdb.set_trace()
            # create object to hold the results from this file/image
            result_file = ResultFile(file_name)
            result_file.name = file_name

            # check all the next lines for boxes/results
            # stop when a new file/image is reached
            temp_idx = i + 1
            while not results_file[temp_idx].find("jpg") > 0:
                # print(result_file.name)
                # print(results_file[temp_idx])
                # search for strings instead of optimistic indexing
                x_left_idx_start = results_file[temp_idx].find("left_x:")
                x_left_idx_end = x_left_idx_start + 7 
                y_top_idx_start = results_file[temp_idx].find("top_y:") 
                y_top_idx_end = y_top_idx_start + 6 
                width_idx_start = results_file[temp_idx].find("width:") 
                width_idx_end = width_idx_start + 6 
                height_idx_start = results_file[temp_idx].find("height:") 
                height_idx_end = height_idx_start + 7 
                eof_idx = results_file[temp_idx].find(")\n") 

                # print(results_file[temp_idx][x_left_idx_end:y_top_idx_start])
                # print(results_file[temp_idx][y_top_idx_end:width_idx_start])
                # print(results_file[temp_idx][width_idx_end:height_idx_start])
                # print(results_file[temp_idx][height_idx_end:eof_idx])

                try:
                    xmin = int(results_file[temp_idx][x_left_idx_end:y_top_idx_start])
                    ymin = int(results_file[temp_idx][y_top_idx_end:width_idx_start])
                    xmax = xmin + int(results_file[temp_idx][width_idx_end:height_idx_start])
                    ymax = ymin + int(results_file[temp_idx][height_idx_end:eof_idx])

                    # print(xmin,ymin,xmax,ymax)

                    box = Box()
                    box.xmin = xmin
                    box.ymin = ymin
                    box.xmax = xmax
                    box.ymax = ymax
                    result_file.boxes = np.append(result_file.boxes, box)
                   
                except:
                    # print("END OF FILE")
                    break

                temp_idx += 1

            result_collection.files = np.append(result_collection.files, result_file)
    result_collection.files = sorted(result_collection.files, key=lambda a: a.file_name)
    # import pdb;pdb.set_trace()  
    return result_collection
    

if __name__=='__main__':
    run_get_results("result.txt")
