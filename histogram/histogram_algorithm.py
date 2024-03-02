from PIL import Image
import matplotlib.pyplot as plt

# Define class Picture that reads an image and converts it to a BMP file
class Picture:
    # Define the __init__ method to read the image
    def __init__(self, image_path):
        self.image = Image.open(image_path)
    # Define a method to convert the image to a BMP file
    def convert_to_bmp(self):
        rgb_img = self.image.convert('RGB')
        rgb_img.save('./histogram/image.bmp')

# Define class Histogram that calculates values of each color in the image
class Histogram():
    def __init__(self):
        self.filename = './histogram/image.bmp'
        self.pixel_values = []
    # Define a method to read the BMP file
    def read_bmp(self):
        with open(self.filename, 'rb') as f:
            f.read(14) # Skip bitmap file header
            bmp_header = f.read(40) # Read bitmap info header
            # Extract image width and height from the header
            width, height = (
                int.from_bytes(bmp_header[4:8],
                'little'),
                int.from_bytes(bmp_header[8:12],
                'little')
                )
            # Skip the rest of the header
            f.read(18)
            # Read the pixel values row by row
            for _ in range(height):
                row = []
                for _ in range(width):
                    # Read the pixel values
                    b = int.from_bytes(f.read(1), 'little')
                    g = int.from_bytes(f.read(1), 'little')
                    r = int.from_bytes(f.read(1), 'little')
                    row.append((r, g, b))
                self.pixel_values.append(row)
                # Skip any padding bytes
                f.read(width % 4)
    # Define a method to get the pixel values
    def get_pixels(self):
        return self.pixel_values
    # Define a method to plot the histogram
    def plot(self):
        # Separate the pixel data into three lists, one for each color channel
        red_values = [pixel[0] for row in self.pixel_values for pixel in row]
        green_values = [pixel[1] for row in self.pixel_values for pixel in row]
        blue_values = [pixel[2] for row in self.pixel_values for pixel in row]
        # Plot a histogram for each color channel
        plt.hist(red_values, bins=256, color='red', alpha=0.5)
        plt.hist(green_values, bins=256, color='green', alpha=0.5)
        plt.hist(blue_values, bins=256, color='blue', alpha=0.5)

        # Add a title and labels to the plot
        plt.title('Color Histogram')
        plt.xlabel('Color Value')
        plt.ylabel('Pixel Count')

        plt.show()

        
# debugging
i = Picture('./histogram/sample_image.jpg')
i.convert_to_bmp()
h = Histogram()
h.read_bmp()
pixels = h.get_pixels()
h.plot()