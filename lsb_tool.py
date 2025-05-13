from PIL import Image

END_DELIMITER = "#####"

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)

def encode_lsb(image_path, output_path, message):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    encoded = img.copy()
    width, height = img.size
    pixels = encoded.load()

    binary_message = text_to_binary(message + END_DELIMITER)
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_message):
                break

            r, g, b = pixels[x, y]
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')

            if data_index < len(binary_message):
                r_bin = r_bin[:-1] + binary_message[data_index]
                data_index += 1
            if data_index < len(binary_message):
                g_bin = g_bin[:-1] + binary_message[data_index]
                data_index += 1
            if data_index < len(binary_message):
                b_bin = b_bin[:-1] + binary_message[data_index]
                data_index += 1

            pixels[x, y] = (int(r_bin, 2), int(g_bin, 2), int(b_bin, 2))

        if data_index >= len(binary_message):
            break

    encoded.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode_lsb(image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    binary_data = ''
    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += format(r, '08b')[-1]
            binary_data += format(g, '08b')[-1]
            binary_data += format(b, '08b')[-1]

            if END_DELIMITER in binary_to_text(binary_data):
                break
        if END_DELIMITER in binary_to_text(binary_data):
            break

    decoded_message = binary_to_text(binary_data)
    return decoded_message.replace(END_DELIMITER, '')

if __name__ == "__main__":
    encode_lsb("input.png", "output.png", "Testing LSB")
    message = decode_lsb("output.png")
    print("Decoded message:", message)