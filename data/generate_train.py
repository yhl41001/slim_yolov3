import os


images_path = os.listdir('images')
with open('train.txt', 'w+') as f:
    for image_path in images_path:
        if not image_path.startswith('COCO_val2017'):
            f.write('data/images/'+image_path+'\n')

