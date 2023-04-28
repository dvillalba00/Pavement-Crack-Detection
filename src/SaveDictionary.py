from skimage import io
import os

def saveDictionary(dictionary, dir_path, folder, name):
    '''
    Saves an image or images from a dictionary to a folder in the directory

    Args:
        dictionary: A dictionary where the keys are tuples of (x,y) and the value is an image as a numpy array
        dir_path: the path of the directory the image will be saved in
        folder: Folder path where the file will be saved
        name: naming prefix for the file being saved
    '''
    for key in dictionary:
        file_name = name + "_" + "{:02d}{:02d}".format(key[0], key[1]) + ".tif"
        io.imsave(os.path.join(dir_path, folder, file_name), dictionary[key], check_contrast=False)
