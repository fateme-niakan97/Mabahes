import os
from skimage import io
import matplotlib.pyplot as plt

filename = os.listdir('pictures')
print(filename)
list_of_images = []

for item in filename:
    img = io.imread(item)
    list_of_images.append(img)

print(list_of_images)

# list_pics = io.imread(filename)

