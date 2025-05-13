# LSB Steganography Tool

This project provides a simple implementation of image-based steganography using the Least Significant Bit (LSB) method. It allows encoding and decoding text messages hidden within PNG images by modifying the least significant bits of pixel color values.

## Features

- Encode textual messages into `.png` images using LSB.
- Decode messages from previously encoded images.
- Supports RGB images; automatically converts other formats.

## Requirements

- Python 3.7 or higher
- [Pillow (PIL)](https://python-pillow.org/)

## Installation

Use a Python virtual environment for safe package management:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pillow
```

## Usage

### Encode a message

```python
from lsb_tool import encode_lsb

encode_lsb("input.png", "output.png", "Your secret message")
```

This will embed `"Your secret message"` into `input.png` and save the result as `output.png`.

### Decode a message

```python
from lsb_tool import decode_lsb

message = decode_lsb("output.png")
print("Decoded message:", message)
```

### Encode and decode a message

You can run the script directly:

```bash
python lsb_tool.py
```

By default, this will encode a test message into `input.png` and decode it from `output.png`.

## How It Works

The algorithm encodes each bit of the input message into the least significant bit of each color channel (red, green, blue) of the image pixels. A predefined delimiter (`#####`) is appended to the message to signal the end during decoding.

## Limitations

- Works only with PNG images in RGB mode.
- The size of the message is limited by the number of available pixels (3 bits per pixel).
- Does not support file hiding or encryption.

## Disclaimer

This tool is for educational purposes only. It does not implement cryptographic security and should not be used for sensitive information.
