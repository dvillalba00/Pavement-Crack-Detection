import numpy as np

def heatImage(thresholded_dict):
    heat_dict = {}
    for key in thresholded_dict:
        heat_dict[key] = np.sum(np.sum(thresholded_dict[key]))
    return heat_dict