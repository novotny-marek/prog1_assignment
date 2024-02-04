import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

class ImageReader:
    def __init__(self, path):
        self.image = iio.imread(path)
    
    def show_image(self):
        plt.imshow(self.image)
        plt.show()

class ImageHistogram(ImageReader):
    def __init__(self, path):
        ImageReader.__init__(self, path)

    def get_histogram(self):
        colors = ('r', 'g', 'b')
        plt.figure()
        plt.xlim([0, 256])

        for i, color in enumerate(colors):
            histogram, bin_edges = np.histogram(
                self.image[:, :, i], bins=256, range=(0, 256)
            )
            plt.plot(bin_edges[0:-1], histogram, color=color)

        plt.title('Color Histogram')
        plt.xlabel('Color Value')
        plt.ylabel('Pixel Count')
        plt.show()


# ImageReader('sample_image.jpg').show_image()

ImageHistogram('sample_image.jpg').show_image()