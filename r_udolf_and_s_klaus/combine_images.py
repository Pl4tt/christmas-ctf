import os
from pathlib import Path
from PIL import Image, ImageChops
from pyzbar.pyzbar import decode


HOME_DIR = Path(__file__).resolve().parent


def xor_images(file_1, file_2, save_file):
    with (
        Image.open(file_1, "r").convert("1") as img_1,
        Image.open(file_2, "r").convert("1") as img_2
        ):
        result = ImageChops.logical_xor(img_1, img_2)

        result.save(save_file)

def scan_qrcode(filename):
    with Image.open(filename) as img:
        data = decode(img)
    
    return data

def save_code(filename, code):
    with open(filename, "x") as file:
        file.write(code)


if __name__ == "__main__":
    img_1 = os.path.join(HOME_DIR, "image_1.png")
    img_2 = os.path.join(HOME_DIR, "image_2.png")
    qrcode_file = os.path.join(HOME_DIR, "target_qrcode.png")
    target_code_file = os.path.join(HOME_DIR, "target_code.txt")

    xor_images(img_1, img_2, qrcode_file)
    data = scan_qrcode(qrcode_file)

    code = data[0].data.decode("utf-8")

    save_code(target_code_file, code)