# SignalGuard AI

## Overview

SignalGuard AI is a Python-based desktop application developed for monitoring and visualizing Distributed Acoustic Sensing (DAS) data. The application reads compressed `.dat` files, processes the signal, extracts useful features, detects abnormal events, and displays multiple signal visualizations through a Tkinter GUI.


# SignalGuard AI

## Demo


https://github.com/user-attachments/assets/4213182d-c22f-4a6c-a62c-708ea424b855


## Features

- Read and parse `.dat` DAS recordings
- Signal normalization and filtering
- Signal vs Distance visualization
- FFT (Fast Fourier Transform)
- Spectrogram
- Derived Phase Trend visualization
- Feature extraction (RMS, Peak, Energy, Mean, Standard Deviation)
- Threshold-based alarm detection
- CSV alarm logging
- Interactive Tkinter GUI

---

## Project Structure

```
SignalGuard-AI/
│
├── core/
├── gui/
├── data/
├── logs/
├── main.py
├── config.py
├── requirements.txt
└── README.md
## Requirements
```
Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running

Place compatible `.dat` files inside the `data/` folder and run:

```bash
python main.py
```

---

## Data Format

The application processes Zstandard-compressed, protobuf-like `.dat` files. Signal samples are extracted from the appropriate data field and visualized after preprocessing.

---

## Note

The provided recordings contain amplitude/intensity samples. Since no confirmed phase field is available in the supplied recordings, the application displays a **Derived Phase Trend** for visualization purposes.

---

## Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib
- Tkinter
- Zstandard

---

## Author

**Gaurish Kale**
kalegaurish03@gmail.com
