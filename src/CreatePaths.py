import os

def createPaths(paths, dir_path):
    for path in paths:
        if not os.path.exists(os.path.join(dir_path , path)):
            os.makedirs(os.path.join(dir_path , path))
