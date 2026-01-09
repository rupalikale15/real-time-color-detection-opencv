import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("../outputs/color_log.csv",
                 names=["R", "G", "B", "Color"])

# Count colors
color_counts = df["Color"].value_counts()

# Plot
plt.figure()
color_counts.plot(kind="bar")
plt.xlabel("Color")
plt.ylabel("Count")
plt.title("Detected Color Frequency")
plt.tight_layout()

# Save graph
plt.savefig("../outputs/color_frequency.png")
plt.show()
