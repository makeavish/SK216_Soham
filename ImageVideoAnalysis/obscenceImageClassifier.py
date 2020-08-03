# -*- coding: utf-8 -*-
"""ObsceneImageClassifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qngPkaYhdXkHkKcHdNUatOhQpje-hpRP
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from keras.preprocessing.image import ImageDataGenerator
from keras.backend import clear_session
from keras.optimizers import SGD, Adam
from pathlib import Path
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.models import Sequential, Model, load_model
from keras.layers import Dense, Dropout, Flatten, AveragePooling2D, BatchNormalization
from keras import initializers, regularizers
from pathlib import Path
from keras.callbacks import ModelCheckpoint, TensorBoard, ReduceLROnPlateau, History, LearningRateScheduler
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import os
import matplotlib.image as mpimg

from google.colab import drive
drive.mount('/content/drive')

train_neutral = (len([iq for iq in os.scandir('/content/drive/My Drive/data/train/neutral')]))
test_neutral = (len([iq for iq in os.scandir('/content/drive/My Drive/data/test/neutral')]))
train_porn = (len([iq for iq in os.scandir('/content/drive/My Drive/data/train/porn')]))
train_sexy = (len([iq for iq in os.scandir('/content/drive/My Drive/data/train/sexy')]))
test_porn = (len([iq for iq in os.scandir('/content/drive/My Drive/data/test/porn')]))
test_sexy = (len([iq for iq in os.scandir('/content/drive/My Drive/data/test/sexy')]))

train_data = [train_neutral, train_porn, train_sexy]
test_data = [test_neutral, test_porn, test_sexy]

print("Total number of train data is : ", train_data[0], "+", train_data[1], "+", train_data[2],"=", sum(train_data))
print("Total number of test data is : ", test_data[0], "+", test_data[1], "+", test_data[2],"=", sum(test_data))

train_path =r"/content/drive/My Drive/data/train"
test_path = r"/content/drive/My Drive/data/test"

"""So we Have 107k images to train and have 6k images to test"""

print("Example of the data Neutral and Sexy category")
f, (ax1, ax2) = plt.subplots(1, 2)
img=mpimg.imread(test_path+"/neutral/ffdb5729-8bac-4add-bbc1-41d1e428c842.jpg")
ax1.imshow(img)
img=mpimg.imread(test_path+"/sexy/ffc15b09-10a0-4753-9adf-d38eb53cf8a1.jpg")
ax2.imshow(img)

"""We need a fast model which gives high accuracy and also have less parsms to train. <br>
We are choosing MobileNet for it.<br>
We will use Transfer Learning and choose weights which were trained for ImageNet.
"""

# As we know the input size in ImageNet was 224 so we have to resize our images accordingly
size = 224
epochs = 10
steps = 500

# We have to take in account different angle of images and to avoid overfit we will use Data Generator, 
# More the Merrier
train_data_generation = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    channel_shift_range=20,
    horizontal_flip=True
)
validation_data_generation = ImageDataGenerator(
    rescale=1./255 #need float values
)

train_generator = train_data_generation.flow_from_directory(
        train_path,
        target_size=(size, size),
        class_mode='categorical',
        batch_size = 64
    )

validation_generator = validation_data_generation.flow_from_directory(
    test_path,
    target_size=(size, size),
    class_mode='categorical',
    batch_size = 64
)

# from keras.backend import clear_session
# clear_session()
# import tensorflow as tf
# from keras.backend.tensorflow_backend import set_session
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
# sess = tf.Session(config=config)
# set_session(sess)  # set this TensorFlow session as the default session for Keras

model.load_weights(resume_weights)

"""## DL Model"""

conv_m = MobileNetV2(weights='imagenet', include_top=False, input_shape=(size, size, 3))
conv_m.trainable = False
conv_m.summary()

model = Sequential()
model.add(conv_m)
model.add(AveragePooling2D(pool_size=(7, 7)))
model.add(Flatten())
model.add(Dense(32, activation = 'relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))
model.summary()

from time import time
filepath = "bestweight.h5"
checkpoint = ModelCheckpoint("weights{epoch:05d}.h5", monitor='val_acc', verbose=1, save_best_only=True, mode='max')
lr_reduce = ReduceLROnPlateau(monitor='val_loss', factor=np.sqrt(0.1), patience=5, verbose=1, cooldown=0, min_lr=0.5e-6)
callbacks = [checkpoint, lr_reduce]

model.compile(
    loss='categorical_crossentropy',
    optimizer=SGD(lr = 0.1, momentum = 0.9),
    metrics=['accuracy']
)

model = load_model("/content/drive/My Drive/Final_weights.h5")

start = datetime.now()
history = model.fit_generator(
    train_generator,
    callbacks=callbacks,
    epochs=50,
    steps_per_epoch=10,
    validation_data=validation_generator,
    validation_steps=10,
    initial_epoch = 0
)

print("time taken : ", datetime.now() - start)

history = model.fit_generator(
    train_generator,
    callbacks=callbacks,
    epochs=100,
    steps_per_epoch=10,
    validation_data=validation_generator,
    validation_steps=10,
    initial_epoch = 78
)

# model.save("nsfwnsfw_mobilenet2_100.h5")



model = load_model("Final_weights.h5")

import coremltools
model.author = "Lakshay Chhabra"
model.short_description = "NSFW Image Classifier"

output_labels = ['Neutral', 'Porn', 'Sexy']
ios = coremltools.converters.keras.convert(model, input_names=['image'], output_names=['output'], 
                                                   class_labels=output_labels, image_input_names='image', image_scale=1/255.0)

ios.save('NSFW.mlmodel')



test_file = test_path+"/sexy/ffc15b09-10a0-4753-9adf-d38eb53cf8a1.jpg"

# https://stackoverflow.com/a/53403805/7437264
from PIL import Image
import numpy as np
from skimage import transform
def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (224, 224, 3))
    np_image = np.expand_dims(np_image, axis=0)
    img=mpimg.imread(filename)
    plt.imshow(img)
    return np_image

image = load("2.jpg")
ans = model.predict(image)
maping = {0 : "Neutral", 1 : "Porn", 2 : "Sexy"}
new_ans = np.argmax(ans[0])

print(maping[new_ans], np.round(ans,2))
print("With {} probability".format(ans[0][new_ans]))

"""# Summary
1. This Model unable to classify drawings and Anime as it is not trained for them.
2. It fails to classify Male genitalia because images in train data are mostly of females.
3. The accuracy can further be improved as I was limited by resources and don't have a GPU, so further training can increase accuracy.
4. Future Goals : To add bounded box with help or YOLO or Sliding window or any other object detection algo and classify video data live.
"""

