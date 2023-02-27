from skimage.filters import threshold_multiotsu
from CreatePaths import createPaths
from LoadImage import loadImage
from SaveCutImages import saveCutImages
from ThresholdCutImages import thresholdCutImages
from SaveThresholdedImages import saveThresholdedImages

# import image
IMAGE_FILE = "../data/Kzoo_Office_v5_orthomosaic.tif"
# horizontal and vertical size cuts to make
DIVIDE_X = 25
DIVIDE_Y = 25

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
