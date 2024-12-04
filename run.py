from Gyeongtaek.detect_items import detect_items
from Jonghwan.draw_items import draw_items
import requests
from PIL import Image

if __name__ == "__main__":
  image_url = "https://djl.ai/examples/src/test/resources/dog_bike_car.jpg"
  image_file = requests.get(image_url, stream=True).raw
  image = Image.open(image_file)
  detected_items = detect_items(image)
  draw_items(image, detected_items)