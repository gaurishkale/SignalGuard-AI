import csv
import os
from datetime import datetime

from config import LOG_FILE


class AlarmLogger:

    def __init__(self):

        if not os.path.exists(LOG_FILE):

            with open(LOG_FILE, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow(
                    ["Timestamp", "RMS", "Peak", "Energy", "Status", "Reason"]
                )

    def log(self, features, status, alarms):

        with open(LOG_FILE, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    round(features["rms"], 4),
                    round(features["peak"], 4),
                    round(features["energy"], 4),
                    "ALARM" if status else "NORMAL",
                    ", ".join(alarms),
                ]
            )
