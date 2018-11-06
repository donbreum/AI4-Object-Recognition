#!/usr/bin/env python3
import cv2
import numpy as np
import os
import sys

from get_ground_truth import *
from get_yolo_results import *

def draw_boxes(image_path, image_name, truth, prediction):
        image = cv2.imread(image_path + image_name)

        # draw bounding box for TRUTH truth - color: GREEN
        for box in truth:
            cv2.rectangle(image, (int(box.xmin), int(box.ymin)), (int(box.xmax), int(box.ymax)), (0, 255, 0), 2)

        # draw bounding box for PREDICTION - color: RED
        for box in prediction:
            cv2.rectangle(image, (int(box.xmin), int(box.ymin)), (int(box.xmax), int(box.ymax)), (0, 0, 255), 2)

        # import pdb; pdb.set_trace()
        # bounding box truth
        # cv2.rectangle(image, (t_xmin, t_ymin), (t_xmax, t_ymax), (0, 255, 0), 2)
        # cv2.rectangle(image, tuple(detection.pred[:2]), 
        #     tuple(detection.pred[2:]), (0, 0, 255), 2)

        # compute the intersection over union and display it
        # iou = bb_intersection_over_union(detection.gt, detection.pred)
        # cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 30),
        #     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        # print("{}: {:.4f}".format(detection.image_path, iou))

        # show the output image
        cv2.imshow(image_name, image)
        cv2.waitKey(0)

def compare_boxes(truth, prediction):
    pass
    # show_result_image(truth, prediction)

def compare_truth_and_prediction():
    annotation_path = sys.argv[1]
    start_file_path = sys.argv[2]
    end_file_path = sys.argv[3]
    result_file_path = sys.argv[4]
    draw_images_path = sys.argv[5]

    truth_files = run_get_ground_truth(annotation_path, start_file_path, end_file_path)
    predicted_files = run_get_results(result_file_path)

    for t_file in truth_files.files:
        for p_file in predicted_files.files:
            if t_file.file_name[:-4] == p_file.file_name[:-4]:
                # compare_boxes(t_file.boxes, p_file.boxes)
                draw_boxes(draw_images_path, p_file.file_name, t_file.boxes, p_file.boxes)
                print(t_file.file_name)
    

if __name__=='__main__':
    # arguments: yolo result file path and path to annotations
    compare_truth_and_prediction()
