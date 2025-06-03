from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def generate_checkerboard(size=256, squares=8):
    pattern = np.indices((size, size)).sum(axis=0) // (size // squares) % 2
    image = np.uint8(pattern * 255)
    return Image.fromarray(image)

def generate_sine_wave_image(width=256, height=256, frequency=5):
    x = np.linspace(0, 2 * np.pi * frequency, width)
    y = np.sin(x)
    img = np.tile(y, (height, 1))
    img = ((img + 1) / 2 * 255).astype(np.uint8)
    return Image.fromarray(img)

def generate_noise_image(size=256):
    img = (np.random.rand(size, size) * 255).astype(np.uint8)
    return Image.fromarray(img)

def save_images():
    os.makedirs("images", exist_ok=True)
    generate_checkerboard().save("images/checkerboard.png")
    generate_sine_wave_image().save("images/sinewave.png")
    generate_noise_image().save("images/noise.png")

if __name__ == "__main__":
    save_images()
    print("✔ Images generated in 'images/' folder")
