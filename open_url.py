"""Script para abrir una dirección del navegador web pásada por parámetros
Pensado para abrir Obsidian, utilizándolo como acceso directo"""

import argparse
import webbrowser

parser = argparse.ArgumentParser(description='Abrir un enlace web')
parser.add_argument('--url', type=str, help='url')
args = parser.parse_args()
webbrowser.open(args.url)