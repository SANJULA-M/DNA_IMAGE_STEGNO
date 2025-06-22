# DNA + Image Steganography in Python using LSB and DNA Cryptography

from PIL import Image
import binascii

# --- DNA Encoding Rules ---
dna_map = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}

reverse_dna_map = {v: k for k, v in dna_map.items()}

# Convert binary to DNA
def binary_to_dna(binary):
    return ''.join(dna_map[binary[i:i+2]] for i in range(0, len(binary), 2))

# Convert DNA back to binary
def dna_to_binary(dna):
    return ''.join(reverse_dna_map[nuc] for nuc in dna)

# --- Convert text to binary ---
def str2bin(message):
    binary = bin(int(binascii.hexlify(message.encode()), 16))[2:]
    while len(binary) % 2 != 0:
        binary = '0' + binary
    return binary

# --- Convert binary to text ---
def bin2str(binary):
    return binascii.unhexlify('%x' % int(binary, 2)).decode()

# --- LSB Encoding ---
def hide_message_dna_lsb(image_path, message):
    img = Image.open(image_path)
    binary = str2bin(message) + '1111111111111110'  # EOF marker
    dna_seq = binary_to_dna(binary)

    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    datas = list(img.getdata())

    new_data = []
    dna_index = 0

    for pixel in datas:
        if dna_index < len(dna_seq):
            r, g, b, a = pixel
            b_bin = format(b, '08b')
            b_bin = b_bin[:-2] + reverse_dna_map[dna_seq[dna_index]]  # embed DNA into 2 LSBs
            b_new = int(b_bin, 2)
            new_data.append((r, g, b_new, a))
            dna_index += 1
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    img.save("stego_dna_output.png")
    print(" Message encoded and saved as 'stego_dna_output.png'")

# --- LSB Decoding ---
def retrieve_message_dna_lsb(image_path):
    img = Image.open(image_path)

    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    datas = list(img.getdata())

    dna_seq = ''

    for pixel in datas:
        b = pixel[2]
        b_bin = format(b, '08b')
        bits = b_bin[-2:]
        dna_seq += dna_map[bits]

        binary_msg = dna_to_binary(dna_seq)
        if binary_msg.endswith('1111111111111110'):
            message = bin2str(binary_msg[:-16])
            print(" Retrieved Message:", message)
            return message

    print(" No hidden message found")
    return ""

# --- Usage Example ---
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="DNA + LSB Image Steganography")
    parser.add_argument('-e', '--encode', metavar='IMAGE', help='Image to encode message into')
    parser.add_argument('-m', '--message', metavar='TEXT', help='Message to hide')
    parser.add_argument('-d', '--decode', metavar='IMAGE', help='Image to decode message from')
    args = parser.parse_args()

    if args.encode and args.message:
        hide_message_dna_lsb(args.encode, args.message)
    elif args.decode:
        retrieve_message_dna_lsb(args.decode)
    else:
        parser.print_help()
