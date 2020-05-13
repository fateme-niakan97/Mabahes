import os
from skimage import io
import matplotlib.pyplot as plt

filename = os.path.join('pictures/1.png')
print('here1')
moon = io.imread(filename)

print(moon.shape)
plt.imshow(moon)
