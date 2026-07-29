import os
import tkinter as tk

from config import RMS_THRESHOLD, PEAK_THRESHOLD

from core.data_loader import FileSource
from core.signal_processor import SignalProcessor
from core.feature_extractor import FeatureExtractor
from core.alarm_engine import AlarmEngine
from core.logger import AlarmLogger

from gui.plots import PlotManager


class SignalGuardApp:

    def __init__(self, root):

        self.root = root
        self.root.title("SignalGuard AI")
        self.root.geometry("1400x850")

        # -------- Top Info Panel --------
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(fill="x", padx=10, pady=5)

        self.status = tk.Label(
            self.info_frame,
            text="Status : READY",
            font=("Arial", 14, "bold"),
        )
        self.status.pack(anchor="w")

        self.feature_label = tk.Label(
            self.info_frame,
            text="",
            font=("Consolas", 11),
            justify="left",
        )
        self.feature_label.pack(anchor="w")

        # -------- Plots --------
        self.plots = PlotManager(root)

        # -------- Backend --------
        self.source = FileSource()
        self.processor = SignalProcessor()
        self.extractor = FeatureExtractor()

        self.alarm = AlarmEngine(
            RMS_THRESHOLD,
            PEAK_THRESHOLD,
        )

        self.logger = AlarmLogger()

        self.update()

    def update(self):

        signal, distance = self.source.next_file()

        signal = self.processor.normalize(signal)
        signal = self.processor.filter(signal)

        freq, spectrum = self.processor.fft(signal)

        _, _, spec = self.processor.spectrogram(signal)

        phase = self.processor.phase_trend(signal)

        features = self.extractor.extract(signal)

        status, alarms = self.alarm.check(features)

        self.logger.log(features, status, alarms)

        current_file = os.path.basename(self.source.files[self.source.index - 1])

        self.feature_label.config(
            text=(
                f"File   : {current_file}\n"
                f"RMS    : {features['rms']:.3f}\n"
                f"Peak   : {features['peak']:.3f}\n"
                f"Energy : {features['energy']:.3f}"
            )
        )

        if status:
            self.status.config(
                text="🔴 ALARM : " + ", ".join(alarms),
                fg="red",
            )
        else:
            self.status.config(
                text="🟢 NORMAL",
                fg="green",
            )

        self.plots.update(
            distance,
            signal,
            freq,
            spectrum,
            spec,
            phase,
        )

        self.root.after(1000, self.update)
