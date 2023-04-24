import os
from skimage import io
from skimage.filters import threshold_multiotsu
from src.CreateImageDict import createImageDict
from src.StitchImageDict import stitchImageDict
from src.CreatePaths import createPaths
from src.LoadImage import loadImage
from src.ThresholdCutImages import thresholdCutImages
from src.ArgParser import parseArgs
from src.SaveDictionary import saveDictionary

dir_path = '/'.join(os.path.realpath(__file__).split('/')[:-1])

# argparser for CLI usage
args = parseArgs()

# set image file name
IMAGES = os.listdir(os.path.join(dir_path , "data" , "raw_images"))
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
image_dict = {}

required_paths = [  # The folders that must exist.
    os.path.realpath("./data"),
    os.path.realpath("./data/raw_images"),  # Where the .tif files will be stored.
    os.path.realpath("./results"),
]
createPaths(required_paths, dir_path)
createImageDict(image_dict, IMAGES)
for image in IMAGES:
    for key in image_dict:
        required_paths.append(image_dict[image]["cut_path"])
        required_paths.append(image_dict[image]["thresholded_cut_path"])
        required_paths.append(image_dict[image]["labeled_cut_path"])
        required_paths.append(image_dict[key]["stitched_path"])
createPaths(required_paths, dir_path)
for key in image_dict:
    image_dict[key]["cut_image_dict"] = loadImage(image_dict[key]["raw_path"], DIVIDE_X, DIVIDE_Y)
    image_dict[key]["thresholded_dict"] = thresholdCutImages(image_dict[key]["cut_image_dict"], thresholding_function)
    # cut_img_dict = loadImage(image_dict[key]["cut_image_dict"], DIVIDE_X, DIVIDE_Y) # image, amount of cuts
    saveDictionary(image_dict[key]["cut_image_dict"], dir_path, image_dict[key]["cut_path"], "cut_image")
    # thresholded_dict = thresholdCutImages(cut_img_dict, thresholding_function) # run cut images through threshold function
    saveDictionary(image_dict[key]["thresholded_dict"], dir_path, image_dict[key]["thresholded_cut_path"], "threshold_image")
    stitched_image = stitchImageDict(image_dict[key]["thresholded_dict"]) # stitch the cut thresholded images back together
    io.imsave(os.path.join(dir_path, image_dict[key]["stitched_path"], key), stitched_image, check_contrast=False)
