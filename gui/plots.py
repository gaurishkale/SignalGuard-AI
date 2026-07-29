import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PlotManager:

    def __init__(self, parent):

        self.figure = Figure(figsize=(12, 8), dpi=100)

        self.ax_signal = self.figure.add_subplot(221)
        self.ax_fft = self.figure.add_subplot(222)
        self.ax_spec = self.figure.add_subplot(223)
        self.ax_phase = self.figure.add_subplot(224)

        self.canvas = FigureCanvasTkAgg(self.figure, master=parent)

        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def update(
        self,
        distance,
        signal,
        freq,
        spectrum,
        spec,
        phase,
    ):

        self.ax_signal.clear()
        self.ax_fft.clear()
        self.ax_spec.clear()
        self.ax_phase.clear()

        # ---------------- Signal ----------------
        self.ax_signal.plot(
            distance,
            signal,
            color="royalblue",
            linewidth=1.2,
        )

        self.ax_signal.set_title("Signal")
        self.ax_signal.set_xlabel("Distance (m)")
        self.ax_signal.set_ylabel("Amplitude")
        self.ax_signal.grid(True)

        # ---------------- FFT ----------------
        self.ax_fft.plot(
            freq,
            spectrum,
            color="darkorange",
            linewidth=1.2,
        )

        self.ax_fft.set_title("FFT")
        self.ax_fft.set_xlabel("Frequency (Hz)")
        self.ax_fft.set_ylabel("Magnitude")
        self.ax_fft.grid(True)

        # ---------------- Spectrogram ----------------
        self.ax_spec.imshow(
            10 * np.log10(spec + 1e-10),
            aspect="auto",
            origin="lower",
            cmap="viridis",
            interpolation="nearest",
            extent=[0, spec.shape[1], 0, 25],
        )

        self.ax_spec.set_title("Spectrogram")
        self.ax_spec.set_xlabel("Time")
        self.ax_spec.set_ylabel("Frequency (Hz)")

        # ---------------- Phase ----------------
        self.ax_phase.plot(
            distance,
            phase,
            color="green",
            linewidth=1.2,
        )

        self.ax_phase.set_title("Derived Phase Trend")
        self.ax_phase.set_xlabel("Distance (m)")
        self.ax_phase.set_ylabel("Phase")
        self.ax_phase.grid(True)

        self.figure.tight_layout()

        self.canvas.draw()
