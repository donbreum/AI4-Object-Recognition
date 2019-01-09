#!/bin/bash

for f in *.jpeg; do
#	echo $f
#	echo "${f%.jpeg}.jpg"
	mv -- "$f" "${f%.jpeg}.jpg"
done
