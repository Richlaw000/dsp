
import numpy as np
import cv2

def generate_checkerboard(size=256, block_size=32):
    image = np.indices((size, size)).sum(axis=0) // block_size % 2
    return (image * 255).astype(np.uint8)

def generate_sine_wave_image(size=256, frequency=10):
    x = np.linspace(0, 2 * np.pi * frequency, size)
    y = np.sin(x)
    image = np.tile(((y + 1) / 2 * 255).astype(np.uint8), (size, 1))
    return image

def generate_noise_image(size=256):
    return (np.random.rand(size, size) * 255).astype(np.uint8)

if __name__ == "__main__":
    cv2.imwrite("images/checkerboard.png", generate_checkerboard())
    cv2.imwrite("images/sine_wave.png", generate_sine_wave_image())
    cv2.imwrite("images/noise.png", generate_noise_image())
