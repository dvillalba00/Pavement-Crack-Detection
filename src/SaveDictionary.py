from skimage import io
import os

def saveDictionary(dictionary, dir_path, folder, name):
    """
    Args:
        Dictionary: A dictionary where the keys are tupples of (x,y) and the value is an image as a numpy array.
        Folder: Path to folder where the file will be saved.
        Name: Naming convention for the files.
    Output:
        None
        Will save the images inside Dictionary into Folder with the name = name + str(key[0]*1000 + key[1])[1:] + ".tif"
    """
    for key in dictionary:
        file_name = name + "_" + "{:02d}{:02d}".format(key[0], key[1]) + ".tif"
        io.imsave(os.path.join(dir_path, folder, file_name), dictionary[key], check_contrast=False)
