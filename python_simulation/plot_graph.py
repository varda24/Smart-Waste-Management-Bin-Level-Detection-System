import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/bin_log.csv")

plt.figure(figsize=(8,5))

plt.plot(
    df.index,
    df["FillPercent"],
    marker="o"
)

plt.title("Waste Bin Fill Level Trend")
plt.xlabel("Readings")
plt.ylabel("Fill Percentage")

plt.grid(True)

plt.savefig("reports/fill_level_graph.png")

plt.show()