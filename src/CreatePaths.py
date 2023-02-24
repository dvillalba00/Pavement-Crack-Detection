import os

paths = [
    "../data",
    "../results",
    "../results/raw_cut_images",
    "../results/thresholded_cut_images"
]

for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)
