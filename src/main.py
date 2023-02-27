import argparse
from skimage.filters import threshold_multiotsu
from CreatePaths import createPaths
from LoadImage import loadImage
from SaveCutImages import saveCutImages
from ThresholdCutImages import thresholdCutImages
from SaveThresholdedImages import saveThresholdedImages

# argparser for CLI usage
parser = argparse.ArgumentParser(description="Thresholds images to find cracks in pavement based on a tiff file image")
parser.add_argument('-x', type=int, help="sets the width value when cutting images")
parser.add_argument('-y', type=int, help="sets the height value when cutting images")
parser.add_argument('-f', '--file', dest="filename", help="name of the image you want to process")
args = parser.parse_args()

# set image file name
filename = args.filename if args.filename else "Kzoo_Office_v5_orthomosaic"
IMAGE_FILE = "../data/{}.tif".format(filename)
# horizontal and vertical size cuts to make
DIVIDE_X = args.x if args.x else 25
DIVIDE_Y = args.y if args.y else 25

# paths to cut image, thresholded cut images
paths = [
    "../data",
    "../results",
    "../results/raw_cut_images",
    "../results/thresholded_cut_images"
]

# user chosen function for thresholding
thresholding_function = threshold_multiotsu

createPaths(paths) # create path for image
cut_img_dict = loadImage(IMAGE_FILE, DIVIDE_X, DIVIDE_Y) # image, amount of cuts
saveCutImages(cut_img_dict) # saving cut image to later threshold
thresholded_dict = thresholdCutImages(cut_img_dict, thresholding_function) # run cut images through threshold function
saveThresholdedImages(thresholded_dict) # save threshold images
