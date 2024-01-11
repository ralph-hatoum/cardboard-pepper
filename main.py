"""good but too costly in time"""

import sys
import time
from turtle import st

def importPackage():
    sys.path.append('/usr/local/lib/python3.11/site-packages')

importPackage()

from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import numpy as np
import cv2
import matplotlib.pyplot as plt

sam_checkpoint = "checkpoints/sam_vit_b_01ec64.pth"
model_type = "vit_b"

images = ["img1.jpg","img2.jpg","img3.jpg","img4.jpg"]

def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    ax.imshow(img)

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
mask_generator = SamAutomaticMaskGenerator(sam)

input_point = np.array([[500, 375]])
input_label = np.array([1])

for img in images:
    start = time.time()
    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = mask_generator.generate(image)
    end_time = time.time()
    elapsed = end_time - start
    print(f"masked {img} in {elapsed} seconds")
    print(masks)

# plt.figure(figsize=(20,20))
# plt.imshow(image)
# show_anns(masks)
# plt.axis('off')
# plt.show() 


