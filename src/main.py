import os
from skimage.filters import threshold_multiotsu
from CreatePaths import createPaths
from LoadImage import loadImage
from SaveCutImages import saveCutImages
from ThresholdCutImages import thresholdCutImages
from SaveThresholdedImages import saveThresholdedImages
from ArgParser import parseArgs

dir_path = '/'.join(os.path.realpath(__file__).split('/')[:-2])

# argparser for CLI usage
args = parseArgs()

# set image file name
filename = args.filename if args.filename else "Kzoo_Office_v5_orthomosaic"
IMAGE_FILE = "{dir}/data/{name}.tif".format(dir=dir_path, name=filename)
# horizontal and vertical size cuts to make
DIVIDE_X = args.x if args.x else 25
DIVIDE_Y = args.y if args.y else 25

# paths to cut image, thresholded cut images
paths = [
    "/data",
    "/results",
    "/results/raw_cut_images",
    "/results/thresholded_cut_images"
]

# user chosen function for thresholding
thresholding_function = threshold_multiotsu

createPaths(paths, dir_path) # create path for image
cut_img_dict = loadImage(IMAGE_FILE, DIVIDE_X, DIVIDE_Y) # image, amount of cuts
saveCutImages(cut_img_dict, dir_path) # saving cut image to later threshold
thresholded_dict = thresholdCutImages(cut_img_dict, thresholding_function) # run cut images through threshold function
saveThresholdedImages(thresholded_dict, dir_path) # save threshold images
