import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config


sp_oauth = SpotifyOAuth(client_id=config('SPOTIPY_CLIENT_ID'), 
                        client_secret=config('SPOTIPY_CLIENT_SECRET'),
                        redirect_uri=config('REDIRECT_URI'),
                        scope=config('SCOPE'))


token_info = sp_oauth.get_access_token(as_dict=False)


sp = spotipy.Spotify(auth=token_info)

user_info = sp.current_user()
user_id = user_info['id']

song_list = ["All my love", "Boulevard of broken dreams", "Chains of love", "Der Kommissar", "Everlasting love", "Fool in the rain", "Good feeling",
              "House of memories", "I like Chopin", "Just what I needed", "Kyrie", "Life is a highway", "Misty mountain hop", "Never gonna give you up", 
              "One thing leads to another", "Private eyes", "Quit playing games with my heart", "Rock me Amadeus", "Stairway to Heaven", "Take me home tonight",
                "Union of the snake", "Vienna calling", "Who can it be now?", "Your love", "Zero the Hero"]


playlist_name = input("Playlist name\n")
phrase = input("Phrase you want\n")


charac = []

for char in phrase:
    if char != " ":
        charac.append(char)


playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
playlist_id = playlist['id']

tracks = []

for letter in charac:
    for palabra in song_list:
        if palabra.startswith(letter.upper()):
            song = palabra
            
            
    results = sp.search(q=f"track:{song}", type='track', market='US')
    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        track_name = track_info['name']
        track_id = track_info['id']

    tracks.append(track_id) 

sp.user_playlist_add_tracks(user_id, playlist_id, tracks)

