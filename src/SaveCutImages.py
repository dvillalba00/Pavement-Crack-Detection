from LoadImage import cut_img_dict
import skimage
from skimage import io

# TODO: Replace '100' with the lowest power of 10 that is greater than max x or y.
for key in cut_img_dict:
    name = str(100 + key[0])[-2:] + str(100 + key[1])[-2:]
    io.imsave("../results/cut_img_" + name  + ".tif", cut_img_dict[key])
