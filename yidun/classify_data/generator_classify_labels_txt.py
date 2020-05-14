# coding: utf-8
"""根据crop_images训练集的图片生成训练用labels"""

import random
import os

TRAIN_PATH = './crop_images/'

images = os.listdir(TRAIN_PATH)
images.remove('.gitignore')

words = set()
for image_name in images:
    _, unicode_name = image_name[:-4].split('_')
    words.add(unicode_name)

print(len(words))
print(words)
with open('./labels.txt', 'w+') as f:
    for word in words:
        f.write('{}\n'.format(word))


