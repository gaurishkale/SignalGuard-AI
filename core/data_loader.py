import os
import numpy as np
import zstandard as zstd

from config import DATA_DIR, DISTANCE_PER_BIN


def read_varint(data, pos):
    """Read protobuf varint."""
    value = 0
    shift = 0

    while True:
        byte = data[pos]
        pos += 1

        value |= (byte & 0x7F) << shift

        if (byte & 0x80) == 0:
            break

        shift += 7

    return value, pos


def skip_field(data, pos, wire_type):
    """Skip unsupported protobuf fields."""

    if wire_type == 0:
        _, pos = read_varint(data, pos)

    elif wire_type == 1:
        pos += 8

    elif wire_type == 2:
        length, pos = read_varint(data, pos)
        pos += length

    elif wire_type == 5:
        pos += 4

    else:
        raise RuntimeError(f"Unsupported protobuf wire type {wire_type}")

    return pos


def parse_dat_file(filepath):
    """
    Reads TTSPL DAS .dat file.

    Returns
    -------
    amplitude : np.ndarray (float32)
    distance  : np.ndarray (meters)
    """

    with open(filepath, "rb") as f:
        compressed = f.read()

    raw = zstd.ZstdDecompressor().decompress(compressed)

    pos = 0

    while pos < len(raw):

        tag, pos = read_varint(raw, pos)

        field_number = tag >> 3
        wire_type = tag & 0x07

        if field_number != 7:
            pos = skip_field(raw, pos, wire_type)
            continue

        if wire_type != 2:
            raise RuntimeError("Field 7 is not length-delimited.")

        length, pos = read_varint(raw, pos)

        payload = raw[pos : pos + length]
        pos += length

        amplitude = np.frombuffer(payload, dtype=np.uint8)

        print(f"Loaded {len(amplitude)} samples")

        amplitude = amplitude.astype(np.float32)

        distance = np.arange(len(amplitude), dtype=np.float32)
        distance *= DISTANCE_PER_BIN

        return amplitude, distance

    raise RuntimeError("Field 7 not found.")


class FileSource:

    def __init__(self, folder=DATA_DIR):

        self.files = sorted(
            os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".dat")
        )

        if not self.files:
            raise FileNotFoundError(f"No .dat files found in '{folder}'")

        self.index = 0

    def next_file(self):

        if self.index >= len(self.files):
            self.index = 0

        file = self.files[self.index]
        self.index += 1

        return parse_dat_file(file)
