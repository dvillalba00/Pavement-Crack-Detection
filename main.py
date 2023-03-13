import os
from skimage.filters import threshold_multiotsu
from src.CreatePaths import createPaths
from src.LoadImage import loadImage
from src.SaveCutImages import saveCutImages
from src.ThresholdCutImages import thresholdCutImages
from src.SaveThresholdedImages import saveThresholdedImages
from src.ArgParser import parseArgs
from src.TestImages import loadLabeledImages, saveLabeledCutImages, testImages

dir_path = '/'.join(os.path.realpath(__file__).split('/')[:-1])

# argparser for CLI usage
args = parseArgs()

# set image file name
filename = args.filename
IMAGE_FILE = "{dir}/data/{name}.tif".format(dir=dir_path, name=filename)
# horizontal and vertical size cuts to make
DIVIDE_X = args.x
DIVIDE_Y = args.y

# paths to cut image, thresholded cut images
paths = [
    "/data",
    "/results",
    "/results/raw_cut_images",
    "/results/thresholded_cut_images",
    "/results/labeled_cut_images"
]

# user chosen function for thresholding
thresholding_function = threshold_multiotsu

createPaths(paths, dir_path) # create path for image
cut_img_dict = loadImage(IMAGE_FILE, DIVIDE_X, DIVIDE_Y) # image, amount of cuts
# saveCutImages(cut_img_dict, dir_path) # saving cut image to later threshold
thresholded_dict = thresholdCutImages(cut_img_dict, thresholding_function) # run cut images through threshold function
# saveThresholdedImages(thresholded_dict, dir_path) # save threshold images
labeled_image_dict = loadLabeledImages(dir_path + '/data/ground_truth', dir_path + '/LabeledImages.txt')
saveLabeledCutImages(labeled_image_dict)

