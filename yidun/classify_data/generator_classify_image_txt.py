# coding: utf-8
import os

files = os.listdir('./images')
files.remove('.gitignore')

with open('./chinese_classify_image.txt', 'w+') as f:
    for file_name in files:
        f.write('classify_data/images/{}\n'.format(file_name))

