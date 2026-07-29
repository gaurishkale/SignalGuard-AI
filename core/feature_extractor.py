import numpy as np


class FeatureExtractor:

    def rms(self, signal):

        return np.sqrt(np.mean(np.square(signal)))

    def peak(self, signal):

        return np.max(np.abs(signal))

    def energy(self, signal):

        return np.sum(np.square(signal))

    def mean(self, signal):

        return np.mean(signal)

    def std(self, signal):

        return np.std(signal)

    def extract(self, signal):

        return {
            "rms": self.rms(signal),
            "peak": self.peak(signal),
            "energy": self.energy(signal),
            "mean": self.mean(signal),
            "std": self.std(signal),
        }
