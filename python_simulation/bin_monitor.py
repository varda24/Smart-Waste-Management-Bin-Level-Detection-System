import pandas as pd
from datetime import datetime
import random
import os

BIN_HEIGHT = 30

distance = random.randint(3, 30)

fill_percent = ((BIN_HEIGHT - distance) / BIN_HEIGHT) * 100

if fill_percent < 50:
    status = "EMPTY"
    alert = "NO ALERT"

elif fill_percent < 80:
    status = "HALF FULL"
    alert = "MONITOR"

else:
    status = "FULL"
    alert = "COLLECTION REQUIRED"

data = {
    "Timestamp": [datetime.now()],
    "Distance": [distance],
    "FillPercent": [round(fill_percent, 2)],
    "Status": [status],
    "Alert": [alert]
}

df = pd.DataFrame(data)

print(df)

csv_file = "data/bin_log.csv"

df.to_csv(
    csv_file,
    mode="a",
    index=False,
    header=not os.path.exists(csv_file)
)