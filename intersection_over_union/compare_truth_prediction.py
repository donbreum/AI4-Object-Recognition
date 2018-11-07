#!/usr/bin/env python3
import cv2
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

from get_ground_truth import *
from get_yolo_results import *
from calc_iou import bb_intersection_over_union

# IOU_THRESHOLD = 0.5

def draw_box(image_path, image_name, truth, prediction, iou):
        image = cv2.imread(image_path + image_name)
        # draw bounding box for TRUTH truth - color: GREEN
        cv2.rectangle(image, (truth.xmin, truth.ymin), (truth.xmax, truth.ymax), (0, 255, 0), 2)

        # draw bounding box for PREDICTION - color: RED
        cv2.rectangle(image, (prediction.xmin, prediction.ymin), (prediction.xmax, prediction.ymax), (0, 0, 255), 2)
        
        # display iou
        cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow(image_name, image)
        cv2.waitKey(0)

def draw_boxes(image_path, image_name, truth, prediction):
        image = cv2.imread(image_path + image_name)
        
        # draw bounding box for TRUTH truth - color: GREEN
        for box in truth:
            cv2.rectangle(image, (box.xmin, box.ymin), (box.xmax, box.ymax), (0, 255, 0), 2)

        # draw bounding box for PREDICTION - color: RED
        for box in prediction:
            cv2.rectangle(image, (box.xmin, box.ymin), (box.xmax, box.ymax), (0, 0, 255), 2)
        cv2.imshow(image_name, image)
        cv2.waitKey(0)

def compare_boxes(image_path, image_name, truth, prediction, iou_threshold):
    FP = 0 # false positives
    TP = 0 # true positives
    FN = 0 # false negatives
    # TN = 0 # true negatives - implicit
    number_of_truth = len(truth)
    number_of_predictions = len(prediction)

    # print("Size truth: ", len(truth))
    # print("Size pred: ", len(prediction))
    # if truth not empty, calculate intersection over union for boxes
    if not len(truth) == 0:
        # find highest intersection over union
        for i, t_box in enumerate(truth):
            highest_iou = -1
            highest_iou_idx = -1
            # print("i: %i",i)

            for k, p_box in enumerate(prediction):
                if not prediction[k].already_used: 
                    # print("k: %i", k)
                    iou = bb_intersection_over_union(t_box, p_box)
                    # print(iou)
                    if iou > highest_iou and iou > 0:
                        highest_iou = iou
                        highest_iou_idx = k
                else:
                    pass
                    # print("Box already used - ignore")
            
            # draw the highest score if its above threshold
            try:
                if not highest_iou == -1 and highest_iou > iou_threshold:
                    # draw_box(image_path, image_name, t_box, prediction[highest_iou_idx], highest_iou)
                    # print("highest", highest_iou,highest_iou_idx)

                    # "remove" box from list when its above threshold
                    prediction[highest_iou_idx].already_used = True

                    # count up TP with 1
                    TP += 1
            except:
                print("Cannot show image")    
    else:
        # if truth is empty, all predictions is false positives
        FP = len(prediction)
    
    if len(prediction) > TP:
        # the number of predictions more than found is FP
        FP += len(prediction) - TP

    if len(truth) - TP > 0:
        FN = len(truth) - TP

    # print("SCORE: (FP, TP, FN) - ", FP,TP,FN)
    return number_of_truth, number_of_predictions, FP, TP, FN

def calculate_precision(tp, fp):
    return tp/(tp + fp)

def calculate_recall(tp, fn):
    return tp/(tp + fn)

def save_figures(iou_array, recall_array, precision_array, display=True):
    # recall vs. iou threshold
    plt.figure("Recall vs. IOU threshold")
    plt.title("Recall vs. IOU threshold")
    plt.plot(iou_array, recall_array)
    plt.ylabel("Recall")
    plt.xlabel("Intersection over union threshold")
    plt.xlim(0.4, 1)
    plt.ylim(0, 1)
    plt.savefig("recall_vs_iou.png")

    # plt.show()
    # import pdb;pdb.set_trace()
    # recall vs. precision
    plt.figure("Precision vs. Recall")
    plt.title("Precision vs. Recall")
    plt.plot(recall_array, precision_array)
    plt.ylabel("Recall")
    plt.xlabel("Precision")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig("recall_vs_precision.png")

    plt.figure("Precision vs. IOU threshold")
    plt.title("Precision vs. IOU threshold")
    plt.plot(iou_array, precision_array)
    plt.ylabel("Precision")
    plt.xlabel("Intersection over union threshold")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig("precision_vs_iou.png")

    if display:
        plt.show()

def compare_truth_and_prediction():
    annotation_path = sys.argv[1]
    start_file_path = sys.argv[2]
    end_file_path = sys.argv[3]
    result_file_path = sys.argv[4]
    draw_images_path = sys.argv[5]

    iou_array = np.array([],dtype=float)
    recall_array = np.array([],dtype=float)
    precision_array = np.array([],dtype=float)

    iou_threshold = 0.00
    for i in range(20):
        iou_threshold += 0.05
        iou_array = np.append(iou_array, round(iou_threshold,2))

        TOTAL_FP = 0
        TOTAL_TP = 0
        TOTAL_FN = 0
        TOTAL_TRUTH = 0
        TOTAL_PREDICTION = 0

        truth_files = run_get_ground_truth(annotation_path, start_file_path, end_file_path)
        predicted_files = run_get_results(result_file_path)
        for t_file in truth_files.files:
            for p_file in predicted_files.files:
                if t_file.file_name[:-4] == p_file.file_name[:-4]:
                    # print(t_file.file_name)
                    (number_of_truth, number_of_predictions, 
                        FP, TP, FN) = compare_boxes(draw_images_path, 
                                                    p_file.file_name, 
                                                    t_file.boxes, 
                                                    p_file.boxes,
                                                    iou_threshold)
                    # draw_boxes(draw_images_path, p_file.file_name, t_file.boxes, p_file.boxes, False)
                    TOTAL_FP += FP
                    TOTAL_TP += TP
                    TOTAL_FN += FN
                    TOTAL_TRUTH += number_of_truth
                    TOTAL_PREDICTION += number_of_predictions
                    # print("\n")

        print("Final result for file: "
                "(FP, TP, FN, TOTAL TRUTH,"
                " TOTAL PREDICTONS, iou) ", TOTAL_FP, 
                                            TOTAL_TP, 
                                            TOTAL_FN, 
                                            TOTAL_TRUTH, 
                                            TOTAL_PREDICTION,
                                            round(iou_threshold,2))
        
        recall = calculate_recall(TOTAL_TP, TOTAL_FN)
        recall_array = np.append(recall_array, recall)
        precision = calculate_precision(TOTAL_TP, TOTAL_FP)
        precision_array = np.append(precision_array, precision)

    save_figures(iou_array, recall_array, precision_array, False)

if __name__=='__main__':
    # arguments: yolo result file path and path to annotations
    compare_truth_and_prediction()
    # compare_boxes([1],[1,2,3,2,1])
