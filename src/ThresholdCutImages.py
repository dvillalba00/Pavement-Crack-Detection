from LoadImage import cut_img_dict
import numpy as np
from skimage.filters import threshold_multiotsu

thresholded_dict = {}
for key in cut_img_dict:
    if len(np.unique(cut_img_dict[key])) < 3:
        thresholded_dict[key] = None
    else:                         
        image = np.dot(cut_img_dict[key][...,:3], [0.299, 0.587, 0.114])
        thresholds = threshold_multiotsu(image)
        regions = np.digitize(image, bins=thresholds)
        thresholded_dict[key] = regions == 0