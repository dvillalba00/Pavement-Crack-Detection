from skimage import io

def saveThresholdedImages(thresholded_dict, dir_path):
    '''

    Args:
        thresholded_dict: a dictionary that has the key of x&y
        dir_path: the path

    Returns: saves the thresholded image

    '''
# TODO: Replace '100' with the lowest power of 10 that is greater than max x or y.
    for key in thresholded_dict:
        name = str(100 + key[0])[-2:] + str(100 + key[1])[-2:]
        try:
            io.imsave(dir_path + "/results/thresholded_cut_images/cut_img_" + name  + ".tif", thresholded_dict[key], check_contrast=False)
        except:
            print(key)
