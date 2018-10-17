#!/usr/bin/env python3
import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import matplotlib.pyplot as plt
import cv2

options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 750,
    'threshold': 0.15,
    'gpu': 0.8
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

fig, ax = plt.subplots(1)
image = cv2.imread('img.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

results = tfnet.return_predict(image)
for color, result in zip(colors, results):
    tl = (result['topleft']['x'], result['topleft']['y'])
    br = (result['bottomright']['x'], result['bottomright']['y'])
    label = result['label']
    confidence = result['confidence']
    text = '{}: {:.0f}%'.format(label, confidence * 100)
    image = cv2.rectangle(image, tl, br, color, 5)
    image = cv2.putText(
        image, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

ax.imshow(image)
plt.show()