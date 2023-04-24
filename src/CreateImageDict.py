import os

def createImageDict(image_dict, IMAGES):
  for image in IMAGES:
      # Name the image
      image_dict[image] = {}
      image_dict[image]["file_name"] = image  # Redundent for the sake of clarity
      image_dict[image]["name"] = image.split('.')[0]  # Without the .tif
      
      # Name the paths
      image_dict[image]["raw_path"] = os.path.join("data" , "raw_images", image_dict[image]["file_name"])
      image_dict[image]["cut_path"] = os.path.join("results" , image_dict[image]["name"], "raw_cut_images")
      image_dict[image]["thresholded_cut_path"] = os.path.join("results" ,  image_dict[image]["name"] , "thresholded_cut_images")
      image_dict[image]["labeled_cut_path"] = os.path.join("results" ,  image_dict[image]["name"] , "labeled_cut_images")
      image_dict[image]["stitched_path"] = os.path.join("results" ,  image_dict[image]["name"] , "stitched_image")