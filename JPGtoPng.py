import sys
import os
from sys import argv 
from PIL import Image

directory = sys.argv[1]
save_directory = sys.argv[2]

if not os.path.isdir(save_directory):
    os.mkdir(save_directory)
for file in os.listdir(directory):
    img = Image.open(f'{directory}/{file}')
    base = os.path.splitext(file)[0]
    img.save(f'{save_directory}/{base}.png','png')