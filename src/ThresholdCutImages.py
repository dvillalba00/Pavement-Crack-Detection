import numpy as np

def thresholdCutImages(cut_img_dict, thresholding_function):
    thresholded_dict = {}
    for key in cut_img_dict:
        if len(np.unique(cut_img_dict[key])) < 3:
            thresholded_dict[key] = None 
        else:                         
            image = np.dot(cut_img_dict[key][...,:3], [0.299, 0.587, 0.114])
            thresholds = thresholding_function(image)
            if not type(thresholds) == type(np.array([])):
                thresholds = [thresholds]
            regions = np.digitize(image, bins=thresholds)
            thresholded_dict[key] = regions == 0
        
        if type(thresholded_dict[key]) == type(None):
            thresholded_dict[key] = np.full(cut_img_dict[key].shape[:2], False)
    
    return thresholded_dict
