from flask import Flask, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="40f5a4a6332b4e81830a758a565f4503",
    client_secret="3a8931ee472b4d688b299637d5c5f2f0",
    redirect_uri="https://yourrenderapp.onrender.com/callback",
    scope="user-read-playback-state user-modify-playback-state"
))

@app.route('/nowplaying')
def now_playing():
    track = sp.current_playback()
    if track and track['is_playing']:
        return jsonify({
            'name': track['item']['name'],
            'artist': track['item']['artists'][0]['name']
        })
    return jsonify({'name': 'No track', 'artist': ''})

@app.route('/playpause')
def playpause():
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()
    return "OK"

@app.route('/next')
def next_track():
    sp.next_track()
    return "OK"

@app.route('/prev')
def prev_track():
    sp.previous_track()
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)