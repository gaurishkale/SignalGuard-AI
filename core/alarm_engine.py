class AlarmEngine:

    def __init__(self, rms_threshold, peak_threshold):

        self.rms_threshold = rms_threshold
        self.peak_threshold = peak_threshold

    def check(self, features):

        alarms = []

        if features["rms"] > self.rms_threshold:
            alarms.append("High RMS")

        if features["peak"] > self.peak_threshold:
            alarms.append("High Peak")

        status = len(alarms) > 0

        return status, alarms
