from skimage import io

def saveCutImages(cut_img_dict, dir_path):
    '''

    Args:
        cut_img_dict: a dictionary of the cut images
        dir_path: the path

    Returns: this function saves the cut images

    '''
# TODO: Replace '100' with the lowest power of 10 that is greater than max x or y.
    for key in cut_img_dict:
        name = str(100 + key[0])[-2:] + str(100 + key[1])[-2:]
        io.imsave(dir_path + "/results/raw_cut_images/cut_img_" + name  + ".tif", cut_img_dict[key], check_contrast=False)
