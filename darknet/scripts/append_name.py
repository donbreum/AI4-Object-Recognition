#!/usr/bin/env python3

# from pathlib import Path
# import os
import sys

def append_name(weight_name, file_name):
    lines_out = ""
    with open(file_name, 'r') as fi:
        lines = fi.readlines()
        last_line = lines[-1] #.split(",")'
        index = last_line.find("dummy_name")

        output_line = last_line[:index] + weight_name + last_line[index+10:] + "\n"
        
        lines = lines[:-1]
        lines.append(output_line)
        lines_out = lines

    # import pdb;pdb.set_trace()
    with open(file_name, 'w') as fi:
        fi.write(''.join(lines_out))

if __name__=='__main__':
    weight_name = sys.argv[1]
    file_name = sys.argv[2]
    append_name(weight_name, file_name)