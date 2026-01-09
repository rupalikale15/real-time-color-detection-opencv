import cv2
import pandas as pd

# Load colors (optional, kept for reference)
colors = pd.read_csv("../data/colors.csv")

cap = cv2.VideoCapture(0)

clicked = False
xpos = ypos = 0

def draw_function(event, x, y, flags, param):
    global xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        xpos, ypos = x, y
        clicked = True

cv2.namedWindow("Webcam Color Detection")
cv2.setMouseCallback("Webcam Color Detection", draw_function)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if clicked:
        b, g, r = frame[ypos, xpos]
        b, g, r = int(b), int(g), int(r)
        h, s, v = hsv[ypos, xpos]

        # HSV-based color detection
        if s < 40 and v > 200:
            color_name = "White"
        elif v < 40:
            color_name = "Black"
        elif h < 10:
            color_name = "Red"
        elif h < 25:
            color_name = "Orange"
        elif h < 35:
            color_name = "Yellow"
        elif h < 85:
            color_name = "Green"
        elif h < 125:
            color_name = "Blue"
        else:
            color_name = "Purple"

        # Save to CSV
        with open("color_log.csv", "a") as f:
            f.write(f"{r},{g},{b},{color_name}\n")

        cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)
        text_color = (255, 255, 255) if r + g + b < 600 else (0, 0, 0)
        text = f"{color_name} | R={r} G={g} B={b}"
        cv2.putText(frame, text, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    cv2.imshow("Webcam Color Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
