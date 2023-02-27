from skimage.filters import threshold_multiotsu
from CreatePaths import createPaths
from LoadImage import loadImage
from SaveCutImages import saveCutImages
from ThresholdCutImages import thresholdCutImages
from SaveThresholdedImages import saveThresholdedImages

IMAGE_FILE = "../data/Kzoo_Office_v5_orthomosaic.tif"
DIVIDE_X = 25
DIVIDE_Y = 25

paths = [
    "../data",
    "../results",
    "../results/raw_cut_images",
    "../results/thresholded_cut_images"
]

thresholding_function = threshold_multiotsu

createPaths(paths)
cut_img_dict = loadImage(IMAGE_FILE, DIVIDE_X, DIVIDE_Y)
saveCutImages(cut_img_dict)
thresholded_dict = thresholdCutImages(cut_img_dict, thresholding_function)
saveThresholdedImages(thresholded_dict)
