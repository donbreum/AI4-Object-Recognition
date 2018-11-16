#!/bin/bash

# Parse the arguments
while [ "$1" != "" ]; do
    case $1 in
        -d | --datafile )        shift
                                datafile=$1
                                ;;
        -c | --cfgfile )	shift
				cfgfile=$1
                                ;;
        -w | --weights )	shift
				weights=$1
				;;
        * )                     
    esac
    shift
done

cd ..

#../darknet detector train ../cfg/rockwool.data ../cfg/rockwool-yolov3-tiny.cfg ../rockwool-yolov3-tiny_1500.weights
#./darknet detector train cfg/$datafile cfg/$cfgfile $weights -dont_show

weights_folder=backup
dummy=dummy

for filename in $weights_folder/*.weights; do
	[ -e "$filename" ] || continue

	./darknet detector map cfg/$datafile cfg/$cfgfile $filename
	dummy=$filename
	# python script here
done

# delete the thresholds that were generated above
if [ -e thresholds.txt ]; then
	rm thresholds.txt
fi

# find weights file with lowest recall score

best_weight=$dummy

for thresh_val in $(seq 0.5 0.01 0.99); do
	
	./darknet detector map cfg/$datafile cfg/$cfgfile $best_weight -thresh $thresh_val
done
