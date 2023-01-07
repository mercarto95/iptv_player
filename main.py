import requests
import os
os.add_dll_directory(os.getcwd())
import vlc

# server information
server_url = "XXXX"
username = "XXXX"
password = "XXXXX"


# Connect to the server and retrieve the list of channels
response = requests.get(f"{server_url}", auth=(username, password))
#channels = response.json()
c = 0
x = open("try3.txt", "w")
for i in response.text:
    try:
        x.write(response.text[c])
        c += 1
    except:
        c += 1
        print("problem")
      
# Create a VLC player instance
player = vlc.MediaPlayer()

channels = ""
# Function to play a channel
def play_channel(channel_id):
  # Get the stream URL for the channel
  stream_url = channels[channel_id]["stream_url"]
  # Load the stream into the player
  player.set_media(vlc.Media(stream_url))
  # Play the stream
  player.play()

# Play the first channel
play_channel(0)