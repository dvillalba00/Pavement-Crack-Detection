from skimage import io
import numpy as np

def stitchImageDict(img_dict, dir_path):
  array_of_rows = []
  count = 0
  dim1, dim2, dim3 = img_dict[(0,0)].shape
  temp_row = np.zeros(shape=(dim1, dim2, dim3))
  for key, value in img_dict.items():
    if(not key[0] == count):
      array_of_rows.append(temp_row)
      count = key[0]
      dim1, dim2, dim3 = img_dict[key].shape
      temp_row = np.zeros(shape=(dim1, dim2, dim3))
    if not temp_row.any():
      temp_row = value
    temp_row = np.concatenate((temp_row, value), axis=1)
  # new_img = np.concatenate((img1, img2), axis=0)
  # io.imsave(dir_path + "/results/stitched_image/stitched_image.tif", new_img, check_contrast=False)