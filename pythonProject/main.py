

import numpy as np
import cv2
import pandas as pd
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras import regularizers
from keras.layers.core import Dropout
from skimage import io
from tensorflow.python.estimator import keras
from keras.models import load_model



model_cancer=tf.keras.models.load_model("Model/cproject.h5")
model_x_Ray=tf.keras.models.load_model("Model/X-Ray.h5")
model_cancer.summary()
print("###############################")
model_x_Ray.summary()

def test_function(file):
    test_image = cv2.imread('images/'+file, cv2.IMREAD_GRAYSCALE )
    img_resized = cv2.resize(test_image, (320,320), )
    img_resized = cv2.bitwise_not(img_resized)
    img_resized = img_resized / 255.0
    img_resized = img_resized.reshape(1,320,320,1)
    ypred = model_cancer.predict(img_resized)
    return (np.argmax(ypred,-1))





def load_image(filename):
    img = tf.keras.preprocessing.image.load_img(filename, target_size=(150, 150))

    img = tf.keras.preprocessing.image.img_to_array(img)

    img = img.reshape(1, 150, 150, 3)

    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img








def result(url):
    img = load_image('images/'+url)
    im = io.imread('images/'+url)
    io.imshow(im)

    result = model_x_Ray.predict(img)
    if (result[0] == 1):
        return ("Patient having Pneumonia.")
    else:
        return ("Normal Patient.")


from flask import Flask,request,jsonify

app = Flask(__name__)
UPLOAD_FOLDER = 'images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


from werkzeug.utils import secure_filename
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded',"result":str(result(file.filename))})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

@app.route('/api/cancer', methods=['POST'])
def upload_file1():
    # check if the post request has the file part
    if 'files' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded',"result":str(test_function(file.filename))})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

if __name__ == "__main__":
    app.run(debug=True)