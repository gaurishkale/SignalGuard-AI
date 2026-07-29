from pathlib import Path


class BinaryInspector:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def inspect(self):

        with open(self.filepath, "rb") as f:
            data = f.read()

        print("=" * 80)
        print(self.filepath.name)
        print("=" * 80)

        print(f"Total Bytes : {len(data)}")

        print("\nHEX DUMP (First 128 bytes)\n")

        for i in range(0, min(128, len(data)), 16):

            chunk = data[i : i + 16]

            hex_values = " ".join(f"{b:02X}" for b in chunk)

            ascii_values = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)

            print(f"{i:04X}   {hex_values:<48}   {ascii_values}")
