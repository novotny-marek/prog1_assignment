# Import necessary libraries
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

# Define a class to read and display an image
class ImageReader:
    # Define the __init__ method to read the image
    def __init__(self, path):
        self.image = iio.imread(path)
    
    # Define a method to display the image
    def show_image(self):
        plt.imshow(self.image)
        plt.show()

# Define a class to create and display a histogram of an image
class ImageHistogram(ImageReader):
    def __init__(self, path):
        # Call the __init__ method of the parent class
        ImageReader.__init__(self, path)

    # Define a method to display the histogram of the image
    def get_histogram(self):
        # Create a new figure and set the x-axis limits
        plt.figure()
        plt.xlim([0, 256])

        # Create a histogram for each color channel
        colors = ('r', 'g', 'b')
        # Loop over each color channel
        for i, color in enumerate(colors):
            # Calculate the histogram for the current color channel
            histogram, bin_edges = np.histogram(
                self.image[:, :, i], bins=256, range=(0, 256)
            )
            # Plot the histogram for the current color channel
            plt.plot(bin_edges[0:-1], histogram, color=color)

        # Add a title and labels to the plot
        plt.title('Color Histogram')
        plt.xlabel('Color Value')
        plt.ylabel('Pixel Count')

        # Display the histogram
        plt.show()


# ImageReader('sample_image.jpg').show_image()
# ImageHistogram('sample_image.jpg').show_image()

ImageHistogram('sample_image.jpg').get_histogram()