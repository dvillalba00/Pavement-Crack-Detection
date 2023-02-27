import os

def createPaths(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
