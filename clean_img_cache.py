"""Simple script to clean the img cache from conversions in recursive conversions"""

import argparse
import os
import webbrowser

parser = argparse.ArgumentParser(description='Simple script to clean the img cache from recursive conversions')
parser.add_argument('--path', type=str, help='path')

args = parser.parse_args()

re_path = args.path
folders = []

for file in os.listdir(re_path):

    file_path = os.path.join(re_path, file)

    if os.path.isdir(file_path):
        folders.append(file_path)

for folder in folders:
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            if file_path.endswith(".jpg") or file_path.endswith(".jpeg") or file_path.endswith(".png") or file_path.endswith(".webp"):
                os.remove(file_path)
