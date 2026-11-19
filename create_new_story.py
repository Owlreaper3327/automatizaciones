"""Personal script to add a new folder structure to my stories in the writing folder and obsidian vault"""

from pathvalidate import sanitize_filename
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--stories_folder', type=str, help='stories folder')
parser.add_argument('--obsidian_folder', type=str, help='vault folder')

args = parser.parse_args()
stories_folder = args.stories_folder
obsidian_folder = args.obsidian_folder

story_name = input("Enter story name: ")

story_name = sanitize_filename(story_name)

final_folder = os.path.join(stories_folder, story_name)
final_obs_folder = os.path.join(obsidian_folder, story_name)

os.mkdir(final_folder)
os.mkdir(final_obs_folder)
os.mkdir(os.path.join(final_folder, "Capítulos"))
os.mkdir(os.path.join(final_folder, "Frases"))
os.mkdir(os.path.join(final_folder, "Playlist"))
os.mkdir(os.path.join(final_obs_folder, "Personajes"))
os.mkdir(os.path.join(final_obs_folder, "Elementos de la trama"))

with open(os.path.join(final_obs_folder, str(story_name + ".md")), "w") as f:
    f.write("A")