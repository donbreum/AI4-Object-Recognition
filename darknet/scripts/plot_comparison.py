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

    result_tiny160_name = "../final_results/190110_rockwool-yolov3-tiny160_2900_thresholds.txt"
    result_tiny224_name = "../final_results/190110_rockwool-yolov3-tiny224_3900_thresholds.txt"
    result_tiny288_name = "../final_results/190109_rockwool-yolov3-tiny288_3800_thresholds.txt"
    result_tiny352_name = "../final_results/190109_rockwool-yolov3-tiny352_3500_thresholds.txt"
    result_tiny416_name = "../final_results/190110_rockwool-yolov3-tiny416_2400_thresholds.txt"
    result_std_name = "../final_results/190110_rockwool-yolov3_2200_thresholds.txt"

    result_tiny160 = load_threshold_file(result_tiny160_name)
    result_tiny224 = load_threshold_file(result_tiny224_name)
    result_tiny288 = load_threshold_file(result_tiny288_name)
    result_tiny352 = load_threshold_file(result_tiny352_name)
    result_tiny416 = load_threshold_file(result_tiny416_name)
    result_std = load_threshold_file(result_std_name)

    plt.figure("Recall vs. IOU threshold")
    plt.title("Recall vs. IOU threshold")
    plt.plot(result_std[:,THRESHOLD], result_std[:,RECALL_IDX])
    plt.plot(result_tiny160[:,THRESHOLD], result_tiny160[:,RECALL_IDX])
    plt.plot(result_tiny224[:,THRESHOLD], result_tiny224[:,RECALL_IDX])
    plt.plot(result_tiny288[:,THRESHOLD], result_tiny288[:,RECALL_IDX])
    plt.plot(result_tiny352[:,THRESHOLD], result_tiny352[:,RECALL_IDX])
    plt.plot(result_tiny416[:,THRESHOLD], result_tiny416[:,RECALL_IDX])
    plt.ylabel("Recall")
    plt.xlabel("Intersection over union threshold")
    plt.xlim(0.5, 1)
    plt.ylim(0, 1)
    plt.legend(["yolov3_416", "yolov3-tiny_160", "yolov3-tiny_224", "yolov3-tiny_288", "yolov3-tiny_352", "yolov3-tiny_416"],loc='lower left')
    plt.grid()
    plt.savefig("../final_results/comparison.png")
    plt.show()