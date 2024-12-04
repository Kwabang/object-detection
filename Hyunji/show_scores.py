import matplotlib.pyplot as plt

def show_scores(detected_items):
  labels = [item['label'] for item in detected_items]
  scores = [item['score'] for item in detected_items]

  plt.figure(figsize=(10, 6))
  plt.bar(labels, scores, color='skyblue')
  plt.xlabel('Items')
  plt.ylabel('Scores')
  plt.title('Detection Scores')
  plt.ylim(0, 1.1)
  plt.show()
