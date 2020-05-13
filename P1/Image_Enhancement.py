import os
from skimage import io
import matplotlib.pyplot as plt

filename_list = os.listdir('pictures')
print(filename_list)
list_of_images = []

for item in filename_list:
    img = io.imread('pictures\\' + item)
    list_of_images.append(img)

print(len(list_of_images))

# list_pics = io.imread(filename)

