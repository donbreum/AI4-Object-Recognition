#!/bin/bash

cd ..

if [ -e times.txt ]; then
	rm times.txt
fi

if [ -e thresholds.txt ]; then
	rm thresholds.txt
fi

if [ -e results.txt ]; then
	rm results.txt
fi

get_times()
{
    cfgfile=$1
    weightsfile=$2
	echo $cfgfile
    echo $weightsfile
	no_extension="${cfgfile%.*}"
    cat small_test.txt | while read line
    do
        echo $line
        ./darknet detector test cfg/rockwool.data cfg/$cfgfile final_results/$weightsfile "$line" -dont_show
    done

    mv times.txt final_results/times/$no_extension".txt"
}

get_recall()
{
    cfgfile=$1
    weightsfile=$2
	echo $cfgfile
    echo $weightsfile
	no_extension="${cfgfile%.*}"

    ./darknet detector map cfg/rockwool.data cfg/$cfgfile final_results/$weightsfile

    mv thresholds.txt final_results/times/$no_extension"_recall.txt"
}

# get_times rockwool-yolov3-tiny160.cfg 190110_rockwool-yolov3-tiny160_2900.weights
# get_times rockwool-yolov3-tiny224.cfg 190110_rockwool-yolov3-tiny224_3900.weights
# get_times rockwool-yolov3-tiny288.cfg 190109_rockwool-yolov3-tiny288_3800.weights
# get_times rockwool-yolov3-tiny352.cfg 190109_rockwool-yolov3-tiny352_3500.weights
# get_times rockwool-yolov3-tiny416.cfg 190111_rockwool-yolov3-tiny416_3300.weights
# get_times rockwool-yolov3.cfg 190110_rockwool-yolov3_2200.weights


get_recall rockwool-yolov3-tiny160.cfg 190110_rockwool-yolov3-tiny160_2900.weights
get_recall rockwool-yolov3-tiny224.cfg 190110_rockwool-yolov3-tiny224_3900.weights
get_recall rockwool-yolov3-tiny288.cfg 190109_rockwool-yolov3-tiny288_3800.weights
get_recall rockwool-yolov3-tiny352.cfg 190109_rockwool-yolov3-tiny352_3500.weights
get_recall rockwool-yolov3-tiny416.cfg 190111_rockwool-yolov3-tiny416_3300.weights
get_recall rockwool-yolov3.cfg 190110_rockwool-yolov3_2200.weights