from pathlib import Path
import numpy as np


class DatReader:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def file_info(self):
        size = self.filepath.stat().st_size

        print("=" * 60)
        print(f"File : {self.filepath.name}")
        print(f"Size : {size} bytes")
        print("=" * 60)

    def inspect(self):

        for dtype in [
            np.uint8,
            np.int16,
            np.uint16,
            np.float32,
            np.float64,
        ]:

            try:
                data = np.fromfile(self.filepath, dtype=dtype)

                print(f"\nDatatype : {dtype}")

                print("Length :", len(data))

                print("First 20 values")

                print(data[:20])

            except Exception as e:

                print(dtype, e)
