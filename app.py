from flask import Flask, request, render_template
from emotion_detection import detect_emotion
from music_recommender import get_music_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get emotion from image
    
    if len(request.files)>0:
        if 'file' in request.files:
            file = request.files['file']
            file.save("uploaded_image.jpg")
            emotion = detect_emotion("uploaded_image.jpg")
    else:
        emotion = request.form['emotion']
    
    # Get music recommendations
    songs = get_music_recommendations(emotion)
    return render_template('results.html', emotion=emotion, songs=songs)
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
