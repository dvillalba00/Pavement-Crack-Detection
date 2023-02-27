import numpy as np
from skimage.filters import threshold_multiotsu

def thresholdCutImages(cut_img_dict, thresholding_function)
    thresholded_dict = {}
    for key in cut_img_dict:
        if len(np.unique(cut_img_dict[key])) < 3:
            thresholded_dict[key] = None
        else:                         
            image = np.dot(cut_img_dict[key][...,:3], [0.299, 0.587, 0.114])
            thresholds = thresholding_function(image)
            regions = np.digitize(image, bins=thresholds)
            thresholded_dict[key] = regions == 0
    return thresholded_dict
