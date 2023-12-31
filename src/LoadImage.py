import numpy as np
from skimage import io

def loadImage(IMAGE_FILE, DIVIDE_X, DIVIDE_Y):
    '''
    Loads an image and segments that image based on the DIVIDE_X and DIVIDE_Y constants

    Args:
        IMAGE_FILE: the image to be loaded
        DIVIDE_X: number of divisions in the x axis for the image
        DIVIDE_Y: number of divisions in the y axis for the image

    Returns:
        cut_img_dict: dictionary of the segmented image with the key being a tuple of 2 indices
            and the value being an array of the image
    '''
    # Read in the image file.
    img = io.imread(IMAGE_FILE)

    # Create the framework for cutting the image.
    maxx = img.shape[0]
    maxy = img.shape[1]
    x_divide = [round(i) for i in np.linspace(0,maxx, DIVIDE_X + 1)]
    y_divide = [round(i) for i in np.linspace(0,maxy, DIVIDE_Y + 1)]
    x=0
    y=0

    # Create the dictionary to hold the cut images.
    # We may want to add metadata later on
    cut_img_dict = {}

    # Actually cut and add the cut images into the dictionary.
    for x in range(len(x_divide) - 1):
        for y in range(len(y_divide) - 1):
            cut_img_dict[(x,y)] = img[x_divide[x]:x_divide[x+1],y_divide[y]:y_divide[y+1]]

    return cut_img_dict
