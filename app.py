
from flask import Flask, send_file
from generate import generate_checkerboard, generate_sine_wave_image, generate_noise_image
import cv2

app = Flask(__name__)

@app.route("/generate/<image_type>")
def generate(image_type):
    if image_type == "checkerboard":
        img = generate_checkerboard()
    elif image_type == "sine":
        img = generate_sine_wave_image()
    elif image_type == "noise":
        img = generate_noise_image()
    else:
        return "Invalid type", 400
    path = f"images/{image_type}.png"
    cv2.imwrite(path, img)
    return send_file(path, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
