import numpy as np
# from https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
def bb_intersection_over_union(truth, pred):

	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(truth.xmin, pred.xmin)
	yA = max(truth.ymin, pred.ymin)
	xB = min(truth.xmax, pred.xmax)
	yB = min(truth.ymax, pred.ymax)

	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (truth.xmax - truth.xmin + 1) * (truth.ymax - truth.ymin + 1)
	boxBArea = (pred.xmax - pred.xmin + 1) * (pred.ymax - pred.ymin + 1)

	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
	# import pdb; pdb.set_trace()
	# return the intersection over union value
	return iou