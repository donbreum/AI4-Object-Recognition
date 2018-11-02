#!/usr/bin/env python3
# import cv2
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
        self.xmin = np.asarray([],dtype=np.int32)
        self.ymin = np.asarray([],dtype=np.int32)
        self.xmax = np.asarray([],dtype=np.int32)
        self.ymax = np.asarray([],dtype=np.int32)


def run_get_results():
    result_collection = AllResults()

    import pdb;pdb.set_trace()
    

    

if __name__=='__main__':
    run_get_results()
