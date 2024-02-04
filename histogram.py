import imageio as iio
import numpy as np
import matplotlib.pyplot as plt

class ImageReader:
    def __init__(self, path):
        self.image = iio.imread(path)
    
    def show_image(self):
        plt.imshow(self.image)
        plt.show()

ImageReader('sample_image.jpg').show_image()