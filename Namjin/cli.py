from Gyeongtaek.detect_items import detect_items
from Jonghwan.draw_items import draw_items
import requests
from PIL import Image
import argparse
import sys

def cli():
  parser = argparse.ArgumentParser(description='Run the object detection script.')
  parser.add_argument('args', nargs=argparse.REMAINDER, help='Arguments to pass to run.py')
  parsed_args = parser.parse_args()

  if not parsed_args.args:
    print("Error: No arguments provided. Please provide the image URL.")
    sys.exit(1)

  image_url = parsed_args.args[0]
  image_file = requests.get(image_url, stream=True).raw
  image = Image.open(image_file)
  detected_items = detect_items(image)
  draw_items(image, detected_items)