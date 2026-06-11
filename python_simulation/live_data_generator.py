import pandas as pd
import random
import time
from datetime import datetime

csv_file = "data/bin_log_backup.csv"

while True:

    distance = random.randint(2, 30)

    fill_percent = round(
        ((30 - distance) / 30) * 100,
        2
    )

    if fill_percent < 50:
        status = "EMPTY"
        alert = "NO ALERT"

    elif fill_percent < 80:
        status = "HALF FULL"
        alert = "MONITOR"

    else:
        status = "FULL"
        alert = "COLLECTION REQUIRED"

    row = pd.DataFrame([{
        "Timestamp": datetime.now(),
        "Distance": distance,
        "FillPercent": fill_percent,
        "Status": status,
        "Alert": alert
    }])

    row.to_csv(
        csv_file,
        mode="a",
        header=not pd.io.common.file_exists(csv_file),
        index=False
    )

    print(
        f"Distance={distance} | Fill={fill_percent}%"
    )

    time.sleep(5)