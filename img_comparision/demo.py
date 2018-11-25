import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from image_comparision import image_comparison

all_images = []
for i in range(9):
    image = mpimg.imread(str(i + 1) + '.png')
    all_images.append(image)
all_images = np.array(all_images)

for i in range(2, 10):
    images = all_images[:i, :, :, :]
    comparision = image_comparison(images)
    plt.imshow(comparision)
    plt.show()




