import numpy as np
from scipy.signal import butter, filtfilt, spectrogram

from config import SAMPLE_RATE, LOW_CUTOFF, HIGH_CUTOFF


class SignalProcessor:

    def __init__(self):

        nyquist = SAMPLE_RATE / 2

        low = LOW_CUTOFF / nyquist
        high = HIGH_CUTOFF / nyquist

        self.b, self.a = butter(N=4, Wn=[low, high], btype="band")

    def normalize(self, signal):

        signal = signal.astype(np.float32)

        signal -= np.mean(signal)

        std = np.std(signal)

        if std > 0:
            signal /= std

        return signal

    def filter(self, signal):

        return filtfilt(self.b, self.a, signal)

    def fft(self, signal):

        spectrum = np.abs(np.fft.rfft(signal))

        freq = np.fft.rfftfreq(len(signal), d=1 / SAMPLE_RATE)

        return freq, spectrum

    def spectrogram(self, signal):

        f, t, sxx = spectrogram(signal, fs=SAMPLE_RATE, nperseg=128, noverlap=64)

        return f, t, sxx

    def phase_trend(self, signal):
        """
        The provided DAS recordings do not contain
        true phase information. This creates a
        derived trend only for visualization.
        """

        signal = self.normalize(signal)

        phase = np.cumsum(signal)

        phase -= np.mean(phase)

        return phase
