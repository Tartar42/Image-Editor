from PIL import Image, ImageEnhance, ImageFilter
import os
#you have to install PIL for that and for that either anaconda or pip. 

path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f'{filename}')

    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename) [0]

    edit.save(f'{clean_name}_edited.jpg')





#Sources: https://www.youtube.com/watch?v=vEQ8CXFWLZU&list=PLsCTnBEpCwH-MZja6wejVZ6sdMbghuGYd&index=4&t=278s
#Date: 17.04.23