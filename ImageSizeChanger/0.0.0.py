from PIL import Image


def resize(input_image, resize_x, resize_y):
    img = Image.open(input_image)
    resize_box = (resize_x, resize_y)
    resize_img = img.resize(resize_box)
    print(input_image)
    name_img = input_image.replace('.png','')
    resize_img.save(name_img + '.jpg')


resize('asd.png', 200, 200)
