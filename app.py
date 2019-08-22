from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import json
from PIL import Image
import io

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = '1244344096571048ab285'
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def json_2_img(data):
    # find longest track index
    index = 0
    largest = 0
    largest_index = 0
    for track in data["track"]:
        track_length = len(track["event"])
        if (track_length > largest):
            largest_index = index
            largest = track_length
        index += 1
    # intialize variables for note iteration
    totalTime = 0
    times = []
    notes = []
    tpb = data['timeDivision'] 
    # iterate through every note
    for event in data["track"][largest_index]["event"]:
        if (event["type"] == 9):
            note = event["data"][0]
            time = event["deltaTime"]
            totalTime += time
            notes.append(note)
            times.append(totalTime)
    # array manipulation
    times = np.asarray(times)
    times = times / tpb * 2
    notes = np.asarray(notes)
    notes = np.array((times, notes)).T
    notes = notes.astype(int)
    last = notes.item(notes.size - 2)
    # Create image
    img = Image.new("1", (last + 1, 128))
    for note in notes:
        x = note[0]
        y = note[1]
        img.putpixel((x, y), 1)
    return img

def parse_image(path):
    img_raw = tf.io.read_file(path)
    img = tf.image.decode_image(img_raw, channels=1)
    img = (tf.cast(img, tf.float32))
    resized_image = tf.image.resize_with_crop_or_pad(img, 88, 850)    
    return resized_image

@app.route('/', methods=['GET'])
def default():
    return render_template("home.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    if request.method == 'POST':
        return "posted test2"

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return "got API"
    if request.method == 'POST':
        data = request.get_json()
        img = json_2_img(data)
        img_path = './uploads/pic.jpg'
        img.save(img_path, "JPEG")
        parsed_img = parse_image(img_path)
        parsed_img = tf.expand_dims(parsed_img, 0)
        modelfile = 'music_classifier.pkl'
        model = load_model(modelfile)
        predictions = model.predict(parsed_img, steps=1, batch_size=1)
        predictions = predictions[0][0]
        predictions = round(predictions, 2)
        predictions = predictions * 100
        os.remove(img_path)
        return str(predictions)

if __name__ == '__main__':    
    app.run()



