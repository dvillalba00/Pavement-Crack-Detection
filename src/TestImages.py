import numpy as np
import os
from skimage import io

def loadLabeledImages(path, images, color=(0,0,0,255):
    """
    Loads in the the hand traced images and creates a binary image 
    of black pixels vs rest
    Args:
        path - the path to the folder containing ONLY the images.
        images - the path to the file containing the images labeled.
        color - the color the images were labeled in.
    """
    text = open(images,'r')
    labeled_images = [line for line in text.readlines() ]

    labeled_image_dict = {}
    for file in os.listdir(path):
        if file[-4:] in labeled_images:
            key = (int(file[-4:-2]), int(file[-2:]))
            img = io.imread(path + '/' + file)
            labeled_image_dict[key] = img == color
    return labeled_image_dict

def saveLabeledCutImages(labeled_image_dict):
    for key in labeled_image_dict:
        name = "{:02d}{:02d}".format(key[0], key[1])
        io.imsave(dir_path + "/results/labeled_cut_images/labeled_img_" + name + ".tif", thresholded_dict[key], check_contrast=False)
    return None

def testImages(labeled_image_dict, thresholded_dict):
    score_dict = {}
    for key in labeled_image_dict:
        lt = labeled_image_dict[key]
        tt = thresholded_dict[key]
        union = lt | tt
        intersection = lt & tt
        ans = intersection / union 
        score_dict[key] = ans
    return score_dict
    
