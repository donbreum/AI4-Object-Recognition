#!/usr/bin/env python3

import sys
import os
import shutil
import datetime

RECALL_IDX = 3
NAME_IDX = 5

def find_best(path_weight_files, result_file, structure_run, final_path_weight_files):

    with open(result_file, 'r') as fi:
        lines = fi.read().splitlines() 
        line_idx_highest_score = 0
        highest_recall_score = 0
        for i in range(len(lines)):
            list_line = lines[i].split(",")

            if float(list_line[RECALL_IDX]) > highest_recall_score:
                highest_recall_score = float(list_line[RECALL_IDX])
                line_idx_highest_score = i

    final_weight_name = ''.join(lines[line_idx_highest_score].split(",")[-1:])[1:]
    
    now = datetime.datetime.now()
    datetime_stamp = (str(now.year) + "_" +  str(now.month) + "_"
        + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute))

    old_file = path_weight_files + final_weight_name
    new_file = path_weight_files + datetime_stamp + "_" + structure_run + "_best_weight_" + final_weight_name
    
    os.rename(old_file, new_file)

    shutil.move(new_file, final_path_weight_files + "/" + new_file)
    import pdb;pdb.set_trace()
   

if __name__=='__main__':
    # ARGUMENTS
    # 1: PATH TO WEIGHT FILES
    # 2: PATH TO RESULT FILE
    # 3: NAME OF CURRENT STRUCTURE RUN
    # 4: PATH TO FINAL WEIGHT FILE (Where to move it after renaming)
    path_weight_files = sys.argv[1]
    result_file = sys.argv[2]
    structure_run = sys.argv[3]
    final_path_weight_files = sys.argv[4]
    find_best(path_weight_files, result_file, structure_run, final_path_weight_files)