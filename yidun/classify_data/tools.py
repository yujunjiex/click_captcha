# coding: utf-8
import os
import random
import shutil

TRAIN_PATH = './crop_images/'
VALID_PATH = './valid/'


def change_images_name_to_unicode():
    """把crop_images里的图片中的中文替换成四位unicode"""
    global TRAIN_PATH
    images = os.listdir(TRAIN_PATH)
    images.remove('.gitignore')

    for image_name in images:
        unicode_list = [_s.encode('unicode_escape').decode()[2:] for _s in image_name[13:-4]]
        new_name = '_'.join([image_name[:13]] + unicode_list) + '.jpg'
        new_path = os.path.join(TRAIN_PATH, new_name)
        old_path = os.path.join(TRAIN_PATH, image_name)
        os.rename(old_path, new_path)
        print(image_name, new_name)

    # # decode
    # _, *unicode_names = new_path[:-4].split('_')
    # for unicode_name in unicode_names:
    #     print((r'\u' + unicode_name).encode().decode('unicode_escape'))


def move_to_valid(count=300):
    """随机300张到测试集"""
    global TRAIN_PATH
    images = os.listdir(TRAIN_PATH)
    images.remove('.gitignore')

    for image_name in random.sample(images, count):
        old_path = os.path.join(TRAIN_PATH, image_name)
        new_path = os.path.join('./valid/', image_name)
        print(old_path, 'to', new_path)
        shutil.copyfile(old_path, new_path)
        os.remove(old_path)


def generator_train_list(train_file_path='./train.list', train_image_path='classify_data/crop_images/'):
    global TRAIN_PATH
    images = os.listdir(TRAIN_PATH)
    images.remove('.gitignore')

    with open(train_file_path, 'w+') as f:
        for image_name in images:
            f.write('{}\n'.format(train_image_path + image_name))


def generator_valid_list(valid_file_path='./valid.list', valid_image_path='classify_data/valid/'):
    global VALID_PATH
    images = os.listdir(VALID_PATH)
    images.remove('.gitignore')

    with open(valid_file_path, 'w+') as f:
        for image_name in images:
            f.write('{}\n'.format(valid_image_path + image_name))


if __name__ == '__main__':
    generator_train_list()
    generator_valid_list()
