from tensorflow.keras.preprocessing.image import img_to_array
from huggingface_hub import hf_hub_download
from tensorflow.keres.models import load_model
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from textblob import TextBlob
import numpy as np
import os
import cv2

model_path = hf_hub_download(
    repo_id ="shivampr1001/Emo0.1",
    filename = "Emo0.1"
)
model = load_model(model_path)
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
