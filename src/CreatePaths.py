import os

def createPaths(paths, dir_path):
    for path in paths:
        if not os.path.exists(dir_path + path):
            os.makedirs(dir_path + path)
