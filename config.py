import os

# Data Configuration
DATA_DIR = "data"
LOG_DIR = "logs"

DISTANCE_PER_BIN = 0.4
TOTAL_BINS = 20000

# Signal Processing
SAMPLE_RATE = 50
LOW_CUTOFF = 0.1
HIGH_CUTOFF = 5.0

BUFFER_SECONDS = 8
BUFFER_LENGTH = SAMPLE_RATE * BUFFER_SECONDS

# Alarm Thresholds
RMS_THRESHOLD = 1.0
PEAK_THRESHOLD = 3.0

# Log File
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "alarm_log.csv")
