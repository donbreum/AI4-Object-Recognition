#!/usr/bin/env python3
import numpy as np
import os
import sys
import matplotlib
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

def load_threshold_file(file_path):

    data = np.loadtxt(file_path, delimiter=",")

    return data

if __name__=='__main__':

    result_tiny_name = "../final_results/181228_rockwool-yolov3-tiny_1700_thresholds.txt"
    result_std_name = "../final_results/181229_rockwool-yolov3_2700_thresholds.txt"

    result_tiny = load_threshold_file(result_tiny_name)
    result_std = load_threshold_file(result_std_name)

    plt.figure("Recall vs. IOU threshold")
    plt.title("Recall vs. IOU threshold")
    plt.plot(result_tiny[:,THRESHOLD], result_tiny[:,RECALL_IDX])
    plt.plot(result_std[:,THRESHOLD], result_std[:,RECALL_IDX])
    plt.ylabel("Recall")
    plt.xlabel("Intersection over union threshold")
    plt.xlim(0.5, 1)
    plt.ylim(0, 1)
    plt.legend(["yolov3-tiny","yolov3"],loc='lower left')
    plt.grid()
    plt.savefig("../final_results/comparison.png")
    plt.show()