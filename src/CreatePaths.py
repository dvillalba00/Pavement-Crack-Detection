import os

def createPaths(paths, dir_path):
    '''
    Creates the necessary paths in the repository for the program to gather data and organize results

    Params:
        paths: list of required paths to be created in the directory
        dir_path: the current working directory path
    '''
    for path in paths:
        if not os.path.exists(os.path.join(dir_path , path)):
            os.makedirs(os.path.join(dir_path , path))
