import pandas as pd
import random
import time

while True:

    bins = pd.DataFrame({
        "Bin": ["Bin A", "Bin B", "Bin C"],
        "FillPercent": [
            random.randint(10, 100),
            random.randint(10, 100),
            random.randint(10, 100)
        ]
    })

    def get_status(fill):

        if fill < 50:
            return "EMPTY"

        elif fill < 80:
            return "HALF FULL"

        return "FULL"

    bins["Status"] = bins["FillPercent"].apply(get_status)

    bins.to_csv(
        "data/multi_bin_data.csv",
        index=False
    )

    print("\nUpdated Bin Data:")
    print(bins)

    time.sleep(5)