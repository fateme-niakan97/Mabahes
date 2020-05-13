import os
from skimage import io
import matplotlib.pyplot as plt

filename = os.listdir('pictures')
print(filename)
list_of_images = []

for item in filename:
    img = io.imread('pictures\\' + item)
    list_of_images.append(img)

print(len(list_of_images))

# list_pics = io.imread(filename)

