import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter, ImageOps

path = '/Users/devmehta/Desktop/LAB_sem5/Python_prg/python_main/Assignment9/image.jpg' 

def extract_image(path):
    image = Image.open(path)
    image.show(title="Original Image")
    return image

def modified_images(image):
    
    resized_image = image.resize((200, 200))
    resized_image.show(title="Resized Image")

    grayscale_image = ImageOps.grayscale(image)
    grayscale_image.show(title="Grayscale Image")

    blurred_image = image.filter(ImageFilter.GaussianBlur(5))
    blurred_image.show(title="Gaussian Blur")

    edge_image = image.filter(ImageFilter.FIND_EDGES)
    edge_image.show(title="Edge Detection")
    
    return resized_image, grayscale_image, blurred_image, edge_image

def plot_histogram(image):
    
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    image_data = np.array(image)
    
    colors = ('r', 'g', 'b')
    hist_data = []

    for i, color in enumerate(colors):
        hist, _ = np.histogram(image_data[:, :, i].flatten(), bins=256, range=(0, 256))
        hist_data.append(hist)

    plt.plot(hist_data[0], color='red', label='Red Channel')
    plt.plot(hist_data[1], color='green', label='Green Channel')
    plt.plot(hist_data[2], color='blue', label='Blue Channel')
    plt.title('Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Pixels')
    plt.legend()
    plt.show()

    bar_width = 5
    x = np.arange(256)

    plt.bar(x - bar_width, hist_data[0], width=bar_width, color='red', label='Red Channel', alpha=0.8)
    plt.bar(x, hist_data[1], width=bar_width, color='green', label='Green Channel', alpha=0.8)
    plt.bar(x + bar_width, hist_data[2], width=bar_width, color='blue', label='Blue Channel', alpha=0.8)

    plt.title('Histogram (Separate Bars)')
    plt.xlabel('Color Ranges')
    plt.ylabel('Pixels')
    plt.xticks(x[::20])  
    plt.legend()
    plt.tight_layout()  
    plt.show()

print("Name: Dev Mehta\nRoll No: 22BCP282")

image = extract_image(path)
resized_image, grayscale_image, blurred_image, edge_image = modified_images(image)
plot_histogram(image)