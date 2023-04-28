import numpy as np

def stitchRows(img_dict, row, startx = 0, stopx = 24):
    '''
    Helper function to be used in stitchImageDict that creates a row out of images

    params:
        img_dict: the dictionary of the image that will be worked on
        row: index of what row is being worked on
        startx: the starting point on the x axis
        stopx: the stopping point on the x axis

    returns:
        a row of stitched image arrays
    '''
    temp_row = img_dict[(row,0)].copy()
    for x in range(startx + 1, stopx + 1):
        temp_row = np.concatenate((temp_row, img_dict[(row, x)]), axis=1)
    return temp_row

def stitchImageDict(img_dict, starty = 0, stopy = 24):
    '''
    Stitches an image out of multiple segmented images in img_dict

    params:
        img_dict: the dictionary of the image that will be worked on
        starty: the starting point on the y axis
        stopy: the stopping point on the y axis

    returns:
        an array of a stitched image from the img_dict provided
    '''
    img = stitchRows(img_dict, 0)
    for y in range(starty + 1, stopy + 1):
        new_row = stitchRows(img_dict, y)
        img = np.concatenate((img, new_row), axis=0)
    return img
