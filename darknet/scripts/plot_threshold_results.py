#!/usr/bin/env python3
import cv2
import numpy as np
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

THRESHOLD = 0
PRECISION_IDX = 1 
RECALL_IDX = 2


def save_figures(iou_array, recall_array, precision_array, model_name, display=False):
    # recall vs. iou threshold
    plt.figure("Recall vs. IOU threshold")
    plt.title("Recall vs. IOU threshold")
    plt.plot(iou_array, recall_array)
    plt.ylabel("Recall")
    plt.xlabel("Intersection over union threshold")
    plt.xlim(0.5, 1)
    plt.ylim(0, 1)
    plt.savefig(model_name + "_recall_vs_iou.png")

    # plt.show()
    # import pdb;pdb.set_trace()
    # recall vs. precision
    # plt.figure("Precision vs. Recall")
    # plt.title("Precision vs. Recall")
    # plt.plot(recall_array, precision_array)
    # plt.ylabel("Recall")
    # plt.xlabel("Precision")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.savefig("recall_vs_precision.png")

    # plt.figure("Precision vs. IOU threshold")
    # plt.title("Precision vs. IOU threshold")
    # plt.plot(iou_array, precision_array)
    # plt.ylabel("Precision")
    # plt.xlabel("Intersection over union threshold")
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.savefig("precision_vs_iou.png")

#     if display:
#         plt.show()

def load_threshold_file(file_path):

    data = np.loadtxt(file_path, delimiter=",")

    return data
    # with open(file_path) as f:
    #     for line in f:
    #         list_threshold_file = np.add(list_threshold_file, line.split(","))
    #         # print(line.split(","))
    #         # element = line.split(",")
    # # list_threshold_file.astype(float)

if __name__=='__main__':
    threshold_file = sys.argv[1]
    model_name = sys.argv[2]

    data = load_threshold_file(threshold_file)
    # import pdb;pdb.set_trace()
    save_figures(data[:,THRESHOLD], data[:,RECALL_IDX], data[:,PRECISION_IDX], model_name)
