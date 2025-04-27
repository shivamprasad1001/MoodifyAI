
 # **MoodifyAI**
 **Home page**
 ![MoodifyAI Demo](https://raw.githubusercontent.com/shivamprasad1001/MoodifyAI/main/static/Home.png)
 **Result page**
 ![MoodifyAI Result](https://github.com/shivamprasad1001/MoodifyAI/blob/main/static/Result.png)

An AI-powered music recommendation system that detects emotions from facial expressions and suggests songs tailored to the user's mood.

---

## **Features**
- Detects emotions from facial expressions using a pre-trained deep learning model.
- Recommends songs based on the detected emotion by integrating with Spotify.
- Provides a user-friendly web interface for interaction.

---

## **Technologies Used**
- **Backend:** Python, Flask, TensorFlow/Keras
- **Frontend:** HTML, CSS, JavaScript
- **Spotify Integration:** Spotify Web API
- **Model:** Pre-trained emotion detection model (`facial_EmotionClassifer.h5`)

---

## **How It Works**
1. **Emotion Detection:**  
   The system uses a deep learning model to analyze facial expressions and classify them into emotions such as happy, sad, angry, neutral, etc.
   
2. **Spotify API Integration:**  
   Based on the detected emotion, the app queries Spotify's API for songs that match the mood and displays the results.

3. **User Interface:**  
   Users interact with the system via a web interface where they can capture or upload images to detect emotions and get music recommendations.

---

## **Getting Started**

### Prerequisites
- Python 3.x
- Spotify Developer Account
- Flask (`pip install flask`)
- TensorFlow/Keras
- Other dependencies listed in `requirements.txt`.

---

### **Steps to Set Up the Project**

#### **1. Clone the Repository**
```bash
git clone https://github.com/shivamprasad1001/MoodifyAI.git
cd MoodifyAI
```

#### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **3. Get Spotify API Credentials**
- Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
- Log in or create an account.
- Create a new application and note down the **Client ID** and **Client Secret**.
- Add a redirect URI for authentication (e.g., `http://localhost:5000/callback`).

#### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add:
```env
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:5000/callback
```

#### **5. Run the Application**
```bash
python app.py
```
Open your browser and go to `http://localhost:5000`.

---

## **How to Use the Spotify API**

#### **Query Songs Based on Emotion**
The app uses the Spotify Web API to fetch songs:
```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="your_client_id",
    client_secret="your_client_secret"
))

# Fetch songs based on genre or mood
results = sp.search(q="genre:pop", type="track", limit=10)
for track in results['tracks']['items']:
    print(f"{track['name']} by {track['artists'][0]['name']}")
```

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See `LICENSE` for details.

---

## **Acknowledgments**
- [Spotify API Documentation](https://developer.spotify.com/documentation/web-api/)
- TensorFlow/Keras for the emotion detection model.

---
