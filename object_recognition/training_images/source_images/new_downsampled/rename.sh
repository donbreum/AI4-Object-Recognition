#!/bin/bash

for f in DJI_0012*.jpg; do
#	echo $f | cut -f2 -d" "
	name=$(echo $f | cut -f1 -d" ")
	number=0$(echo $f | cut -f2 -d" ")
#	echo $f
#	echo "$name $number"
	mv -- "$f" "$name $number"
#	echo "${f%.jpeg}.jpg"
#	mv -- "$f" "${f%.jpeg}.jpg"

	
done
