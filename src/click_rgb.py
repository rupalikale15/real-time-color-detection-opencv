
import cv2
import pandas as pd

colors = pd.read_csv("../data/colors.csv")
cap = cv2.VideoCapture(0)

clicked = False
xpos = ypos = 0

def get_color_name(R, G, B):
    minimum = 10000
    cname = ""
    for i in range(len(colors)):
        d = abs(R - colors.loc[i, "R"]) + abs(G - colors.loc[i, "G"]) + abs(B - colors.loc[i, "B"])
        if d < minimum:
            minimum = d
            cname = colors.loc[i, "color_name"]
    return cname

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

    if clicked:
        b, g, r = frame[ypos, xpos]
        name = get_color_name(r, g, b)
        cv2.rectangle(frame, (20,20), (750,60), (int(b),int(g),int(r)), -1)
        text = f"{name} | R={r} G={g} B={b}"
        color = (255,255,255) if r+g+b < 600 else (0,0,0)
        cv2.putText(frame, text, (30,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Webcam Color Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
