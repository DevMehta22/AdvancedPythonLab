from PIL import Image, ImageFilter, ImageOps
import matplotlib.pyplot as plt
import numpy as np

def load_and_display_image(image_path):
    image = Image.open(image_path)
    image.show(title="Original Image")
    return image

def apply_image_manipulations(image):
    
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
    
    # Graph: Line Plot for Histogram
    plt.figure(figsize=(10, 5))
    plt.plot(hist_data[0], color='red', label='Red Channel')
    plt.plot(hist_data[1], color='green', label='Green Channel')
    plt.plot(hist_data[2], color='blue', label='Blue Channel')
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.legend()
    plt.grid()
    plt.show()

    # Histogram: Bar Plot for Histogram
    plt.figure(figsize=(10, 5))
    bar_width = 5
    x = np.arange(256)

    plt.bar(x - bar_width, hist_data[0], width=bar_width, color='red', label='Red Channel', alpha=0.8)
    plt.bar(x, hist_data[1], width=bar_width, color='green', label='Green Channel', alpha=0.8)
    plt.bar(x + bar_width, hist_data[2], width=bar_width, color='blue', label='Blue Channel', alpha=0.8)

    plt.title('Color Histogram (Separate Bars)')
    plt.xlabel('Color Value Ranges')
    plt.ylabel('# of Pixels')
    plt.xticks(x[::20], rotation=45)  
    plt.legend()
    plt.grid(axis='y')
    plt.ylim(0, max(max(hist_data[0]), max(hist_data[1]), max(hist_data[2])) * 1.1)  
    plt.tight_layout()  
    plt.show()

def main(image_path):

    image = load_and_display_image(image_path)

    resized_image, grayscale_image, blurred_image, edge_image = apply_image_manipulations(image)

    plot_histogram(image)

image_path = '/Users/devmehta/Desktop/LAB_sem5/Python_prg/python_main/Assignment_data_visualisation/image.jpg'  # Use raw string to avoid issues with backslashes

main(image_path)