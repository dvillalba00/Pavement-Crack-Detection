import numpy as np

def heatImage(thresholded_dict):
    '''
    Creates a dictionary of the sum of the density of detected cracks to form a heat map of the thresholded image

    Params:
        thresholded_dict: dictionary of the thresholded image the heat map will be created from

    returns:
        heat_dict: dictionary of the sum of the density of cracks being detected in a thresholded dictionary
    '''
    heat_dict = {}
    for key in thresholded_dict:
        heat_dict[key] = np.sum(np.sum(thresholded_dict[key]))
    return heat_dict