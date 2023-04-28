import argparse
# argparser for CLI usage
def parseArgs():
  '''
  Allows for the usage of flags in the CLI for easier use of DetectPavementCracks.py with image segmentation

  returns: parser object to be used in DetectPavementCracks.py for determining DIVIDE_X and DIVIDE_Y
  '''
  parser = argparse.ArgumentParser(description="Thresholds images to find cracks in pavement based on a tiff file image")
  parser.add_argument('-x', type=int, help="sets the width value when cutting images", default=25)
  parser.add_argument('-y', type=int, help="sets the height value when cutting images", default=25)
  return parser.parse_args()
