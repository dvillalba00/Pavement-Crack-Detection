import argparse
# argparser for CLI usage
def parseArgs():
  parser = argparse.ArgumentParser(description="Thresholds images to find cracks in pavement based on a tiff file image")
  parser.add_argument('-x', type=int, help="sets the width value when cutting images", default=25)
  parser.add_argument('-y', type=int, help="sets the height value when cutting images", default=25)
  parser.add_argument('-f', '--file', required=True, dest="filename", help="name of the image you want to process")
  return parser.parse_args()
