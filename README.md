# DNA + Image Steganography using LSB Manipulation

This project combines **DNA cryptography** and **image steganography** to securely hide secret messages inside images using **Least Significant Bit (LSB)** manipulation and bio-inspired encoding. The goal is to enhance the confidentiality of hidden data by layering two techniques: DNA-based encryption and image-level steganography.

## Features

- Convert plaintext messages into DNA sequences.
- Embed DNA-encoded binary into the **blue channel** of an image using LSB.
- Supports secure message extraction with an EOF marker.
- Lightweight Python implementation without external encryption libraries.
- Works with `.png` images to avoid data loss.

## Project Structure

DNA_IMAGE_STEGNO/
├── dna_stegno.py # Main Python script
├── stego_dna_output.png # Output image with hidden message
├── input.png # Original cover image
└── README.md # Project documentation

## Requirements

- Python 3.7 or above
- Required Libraries:
  - `Pillow` (for image handling)
  - `binascii` and `argparse` (standard libraries)

## How to run :

| Option              | Description                                    | Example                   |
| ------------------- | ---------------------------------------------- | ------------------------- |
| `-e` or `--encode`  | Path to the image in which to hide the message | `-e input.png`            |
| `-m` or `--message` | The secret message to hide                     | `-m "This is secret"`     |
| `-d` or `--decode`  | Path to the image to extract the message from  | `-d stego_dna_output.png` |

Encode : python dna_stegno.py -e input.png -m "Your secret message here"
Decode : python dna_stegno.py -d stego_dna_output.png
