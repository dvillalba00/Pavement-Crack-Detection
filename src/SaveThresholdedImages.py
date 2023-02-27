from skimage import io

def saveThresholdedImages(thresholded_dict):
# TODO: Replace '100' with the lowest power of 10 that is greater than max x or y.
    for key in thresholded_dict:
        name = str(100 + key[0])[-2:] + str(100 + key[1])[-2:]
        try:
            io.imsave("../results/thresholded_cut_images/cut_img_" + name  + ".tif", thresholded_dict[key])
        except:
            print(key)
