import cv2
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
colors = pd.read_csv("../data/colors.csv")
X = colors[['R', 'G', 'B']]
y = colors['color_name']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

cap = cv2.VideoCapture(0)

def get_dominant_color(frame):
    small = cv2.resize(frame, (50, 50))
    pixels = small.reshape(-1, 3)
    pixels = np.float32(pixels)

    _, _, centers = cv2.kmeans(
        pixels, 1, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        10, cv2.KMEANS_RANDOM_CENTERS
    )
    return centers[0]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    b, g, r = get_dominant_color(frame)
    b, g, r = int(b), int(g), int(r)

    color_name = knn.predict([[r, g, b]])[0]

    cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)
    text_color = (255, 255, 255) if r + g + b < 600 else (0, 0, 0)
    text = f"Dominant: {color_name} | R={r} G={g} B={b}"

    cv2.putText(frame, text, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    cv2.imshow("Webcam Color Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
