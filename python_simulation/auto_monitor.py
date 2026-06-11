import pandas as pd
from datetime import datetime
import random
import time
import os

BIN_HEIGHT = 30

csv_file = "data/bin_log.csv"

while True:

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

    df.to_csv(
        csv_file,
        mode="a",
        index=False,
        header=not os.path.exists(csv_file)
    )

    print(
        f"{datetime.now()} | "
        f"Distance={distance} cm | "
        f"Fill={round(fill_percent,2)}% | "
        f"{status}"
    )

    time.sleep(5)