from skimage import io
import numpy as np

def stitchRows(img_dict, row, startx = 0, stopx = 24):
  temp_row = img_dict[(row,0)].copy()
  for x in range(startx + 1, stopx + 1):
    temp_row = np.concatenate((temp_row, img_dict[(row, x)]), axis=1)
  return temp_row

def stitchImageDict(img_dict, dir_path, starty = 0, stopy = 24):
  img = stitchRows(img_dict, 0)
  for y in range(starty + 1, stopy + 1):
    new_row = stitchRows(img_dict, y)
    img = np.concatenate((img, new_row), axis=0)
  io.imsave(dir_path + "/results/stitched_image/stitched_image.tif", img, check_contrast=False)
