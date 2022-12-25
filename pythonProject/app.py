

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

#
# train_dir = "train"
# validation_dir ="test"
# train_normal_dir = os.path.join(train_dir,'NORMAL')
# train_pneumonia_dir = os.path.join(train_dir,'PNEUMONIA')
# validation_normal_dir = os.path.join(validation_dir, 'NORMAL')
# validation_pneumonia_dir = os.path.join(validation_dir,'PNEUMONIA')
#
#
# train_normal_names = os.listdir(train_normal_dir)
# print(train_normal_names[:10])
#
# train_pneumonia_names = os.listdir(train_pneumonia_dir)
# print(train_pneumonia_names[:10])
#
# print('total training normal-rays :', len(os.listdir(train_normal_dir)))
# print('total training Pneumonia x-rays:', len(os.listdir(train_pneumonia_dir)))
# print('total validation normal-rays :', len(os.listdir(validation_normal_dir)))
# print('total validation Pneumonia x-rays:', len(os.listdir(validation_pneumonia_dir)))
#
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2, 2),
#
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(512, activation='relu'),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])
# model.summary()
#
# model.compile(loss='binary_crossentropy',
#               optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
#               metrics=['accuracy'])
#
# train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1/255)
# validation_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1/255)
#
# train_generator = train_data_generator.flow_from_directory(
#         train_dir,
#         target_size = (150,150),
#         batch_size = 32,
#         class_mode = 'binary')
#
# validation_generator = validation_data_generator.flow_from_directory(
#         validation_dir,
#         target_size = (150,150),
#         batch_size = 32,
#         class_mode = 'binary')
#
# history=model.fit(train_generator,
# epochs = 10,
# validation_data = validation_generator
# )
#
# def load_image(filename):
#     img = tf.keras.preprocessing.image.load_img(filename, target_size=(150, 150))
#
#     img = tf.keras.preprocessing.image.img_to_array(img)
#
#     img = img.reshape(1, 150, 150, 3)
#
#     img = img.astype('float32')
#     img = img - [123.68, 116.779, 103.939]
#     return img
#
#
#
#
#
#
#
#
# def result(url):
#     img = load_image('images/'+url)
#     im = io.imread('images/'+url)
#     io.imshow(im)
#
#     result = model.predict(img)
#     if (result[0] == 1):
#         return ("Patient having Pneumonia.")
#     else:
#         return ("Normal Patient.")

#
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# from werkzeug.utils import secure_filename
#
#
# UPLOAD_FOLDER = 'images/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# @app.route('/')
# def main():
#     return 'Homepage'
#
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # check if the post request has the file part
#     if 'files' not in request.files:
#         resp = jsonify({'message': 'No file part in the request'})
#         resp.status_code = 400
#         return resp
#
#     files = request.files.getlist('files')
#
#     errors = {}
#     success = False
#
#     for file in files:
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             success = True
#         else:
#             errors[file.filename] = 'File type is not allowed'
#
#     if success and errors:
#         errors['message'] = 'File(s) successfully uploaded'
#         resp = jsonify(errors)
#         resp.status_code = 500
#         return resp
#     if success:
#         resp = jsonify({'message': 'Files successfully uploaded',"result":str(result(file.filename))})
#         resp.status_code = 201
#         return resp
#     else:
#         resp = jsonify(errors)
#         resp.status_code = 500
#         return resp
#
# if __name__ == "__main__":
#     app.run(debug=True)


model_cancer=tf.keras.models.load_model("Model/cproject.h5")
model_x_Ray=tf.keras.models.load_model("Model/X-Ray.h5")
model_cancer.summary()
print("###############################")
model_x_Ray.summary()

def test_function(file):
    test_image = cv2.imread(file, cv2.IMREAD_GRAYSCALE )
    img_resized = cv2.resize(test_image, (320,320), )
    img_resized = cv2.bitwise_not(img_resized)
    img_resized = img_resized / 255.0
    img_resized = img_resized.reshape(1,320,320,1)
    ypred = model_cancer.predict(img_resized)
    print(np.argmax(ypred,-1))


test_function("Model/5.png")


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

    from flask import Flask, request, jsonify

    app = Flask(__name__)

    from werkzeug.utils import secure_filename


    UPLOAD_FOLDER = 'images/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    @app.route('/')
    def main():
        return 'Homepage'


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

    if __name__ == "__main__":
        app.run(debug=True)
