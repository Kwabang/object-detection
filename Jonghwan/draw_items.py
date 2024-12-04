import cv2
import numpy as np
from matplotlib import pyplot as plt

def draw_items(image, detected_items):
  image = np.array(image)

  for item in detected_items:
    label = item['label']
    score = item['score']
    box = item['box']
    cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
    
    text = f"{label} {score:.2f}"
    (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)
    cv2.rectangle(image, (int(box[0]), int(box[1]) - text_height - 10), (int(box[0]) + text_width, int(box[1])), (0, 255, 0), cv2.FILLED)
    
    cv2.putText(image, text, (int(box[0]), int(box[1]) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

  plt.imshow(image)
  plt.axis('off')
  plt.show(block=False)