![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-kNN-orange.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

# 🎨 Real-Time Color Detection using OpenCV

A complete computer vision project that demonstrates **real-time color detection** using a webcam.  
The project covers **basic image processing, HSV-based color detection, dominant color extraction, data logging, visualization, and ML-based classification**.

🚀 Beginner → Intermediate → ML-level progression in one repository.

---

## 🔥 Features

✅ Real-time webcam color detection  
✅ Mouse click RGB detection (baseline)  
✅ HSV-based color detection (industry standard)  
✅ Automatic CSV logging of detected colors  
✅ Dominant color detection (no user input)  
✅ Machine Learning classification using kNN  
✅ Data visualization (color frequency graph)  
✅ Demo GIF + screenshots  

---

## 📁 Project Structure

real-time-color-detection-opencv/
│
├── data/
│ └── colors.csv
│
├── src/
│ ├── option_c_click_rgb.py
│ ├── option_a_hsv_csv.py
│ ├── option_b_dominant_ml.py
│ └── plot_color_graph.py
│
├── outputs/
│ └── color_frequency.png
│
├── screenshots/
│ ├── option_c_click.png
│ ├── option_a_hsv.png
│ ├── option_b_ml.png
│ └── demo.gif
│
├── requirements.txt
└── README.md
## 🧪 Implemented Approaches

### 🔹 Option A — HSV + CSV Logging (Recommended)
- Uses HSV color space (robust to lighting)
- Logs detected colors into CSV
- Industry-relevant approach

### 🔹 Option B — Dominant Color + ML (Advanced)
- Automatically detects dominant color in frame
- Uses K-Means clustering
- Classifies color using kNN (Machine Learning)

### 🔹 Option C — Click-Based RGB Detection
- Detects color by clicking on a pixel
- Uses RGB distance matching
- Beginner-friendly baseline

---

## 📊 Data Analysis

Detected color frequency visualization:

![Color Frequency](outputs/color_frequency.png)

Outputs
<img width="1001" height="784" alt="Screenshot 2026-01-09 162024" src="https://github.com/user-attachments/assets/cb1bf77e-6dda-4da7-86aa-10851aa68296" />
<img width="990" height="775" alt="Screenshot 2026-01-09 155511" src="https://github.com/user-attachments/assets/900a7517-ee10-4580-9e4b-c259f75ecb0f" />

---

## ⚙️ Tech Stack

- Python 3
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Run HSV-based detection
cd src
python option_a_hsv_csv.py
3️⃣ Generate color frequency graph
python plot_color_graph.py
4️⃣ Run ML-based dominant color detection
python option_b_dominant_ml.py
---



