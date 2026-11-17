"""Recursive img conversion for comics, like DImage, but without all that messy Python UI"""

import os
import img2pdf
import argparse
from PIL import Image
from tkinter import messagebox as msb


def extract_queue(path:str) -> list[str]:
    """Extract all folders in path"""

    queue = []

    for file in os.listdir(path):

        if os.path.isdir(os.path.join(path, file)):
            path = os.path.join(path, file)
            queue.append(path)

    queue.sort()
    return queue

def convert_webp(path_img:str) -> str:
    """Convert a webp image to .jpeg"""
    img = Image.open(path_img)
    img.convert("RGB")
    name = os.path.basename(path_img)
    final_name = os.path.join(os.path.dirname(path_img), name + ".jpg")
    img.save(final_name, "JPEG")
    return final_name

def extract_img(path:str) -> list[str]:
    """Extract all images in folder path"""
    imgs = []

    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            continue

        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".webp"):
            img = os.path.join(path, file)
            if file.endswith(".webp"):
                img = convert_webp(img)

            imgs.append(img)

    imgs.sort()
    return imgs

def convert_pdf(path:str) -> None:
    """Convert a pack of images into a pdf file"""

    imgs = extract_img(path)
    final_name = os.path.basename(path)
    final_name = os.path.join(path, final_name + ".pdf")

    with open(final_name, "wb") as f:
        f.write(img2pdf.convert(imgs))

def convert(path:str) -> None:
    """Convert a pack of folders with images into several pdf files"""
    queue = extract_queue(path)

    for task in queue:
        convert_pdf(task)

    msb.showinfo(message="All done!")


parser = argparse.ArgumentParser()
parser.add_argument("--path_to_folder", type=str, help="path to folder containing other folders with images")

args = parser.parse_args()
path_to_folder = args.path_to_folder
convert(path_to_folder)