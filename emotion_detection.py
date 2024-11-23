from textblob import TextBlob
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import cv2


# # Load pre-trained model
model = tf.keras.models.load_model("models/facial_EmotionClassifer.h5")

def detect_emotion(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (48, 48))
    img = img_to_array(img)
    img = img/255.0
    img = np.expand_dims(img, axis=0)
    # img = img.reshape(1, 48, 48, 1)
    predictions = model.predict(img)
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    return emotions[predictions.argmax()]



def detect_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative"
