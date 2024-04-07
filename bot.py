import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging
import re
import random

# Discord Bot Token (replace with your own)
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Spotify Credentials (replace with your own)
SPOTIFY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
SPOTIFY_REDIRECT_URI = 'YOUR_SPOTIFY_REDIRECT_URI'
SPOTIFY_PLAYLIST_ID = 'YOUR_SPOTIFY_PLAYLIST_ID'

# Set up Discord intents
intents = discord.Intents.default()
intents.messages = True  # To process messages
intents.message_content = True  # To access the full content of the messages

# List of replies for when the bot is mentioned
# Replace these with your own custom responses
mention_replies = [
    "I'm just a bot, not a real person.",
    "Sorry, I'm busy with other tasks.",
    "I don't have much to say right now.",
    "Error 404: Personality not found.",
    "My programming doesn't allow me to engage in that kind of banter.",
]

# Create the bot with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

@bot.event
async def on_ready():
    """
    Event handler called when the bot is ready and logged in.
    Logs the bot's username and sets up the Spotify authentication.
    """
    logging.info(f'Logged in as {bot.user.name}')
    await setup_spotify_auth()

async def setup_spotify_auth():
    """
    Sets up the Spotify authentication using the provided credentials.
    Triggers the authorization flow and waits for the user to authorize the bot.
    """
    auth_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                               client_secret=SPOTIFY_CLIENT_SECRET,
                               redirect_uri=SPOTIFY_REDIRECT_URI,
                               scope='playlist-modify-public')

    # Trigger the authorization flow
    auth_url = auth_manager.get_authorize_url()
    logging.info(f"Please visit this URL to authorize the bot: {auth_url}")

    # Wait for the user to authorize the bot and get the access token
    auth_response = input("Enter the authorization code: ")
    token_info = auth_manager.get_cached_token()
    if not token_info:
        token_info = auth_manager.get_access_token(auth_response)

    # Create the Spotify client
    global spotify
    spotify = spotipy.Spotify(auth_manager=auth_manager)

@bot.event
async def on_message(message):
    """
    Event handler called whenever a message is received.
    If the bot is mentioned, it sends a random reply from the `mention_replies` list.
    If a Spotify track link is found in the message, it adds the track to the specified playlist.
    """
    # Check if the bot is mentioned directly
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        reply_message = random.choice(mention_replies)
        await message.channel.send(reply_message)

    # Ignore messages from the bot or messages not in the 'music-recommendations' channel
    if message.author == bot.user or message.channel.name != 'music-recommendations':
        logging.debug(f'Ignoring message from {message.author} in channel {message.channel.name}')
        return

    # Use a regular expression to find the Spotify track link
    match = re.search(r'https://open.spotify.com/track/(\w+)', message.content)
    if match:
        track_id = match.group(1)
        logging.debug(f'Found Spotify track link in message: {message.content}')
        try:
            await add_song_to_playlist(track_id)
        except Exception as e:
            logging.error(f'Error adding song to playlist: {e}')
    else:
        logging.debug(f'No Spotify track link found in message: {message.content}')

    await bot.process_commands(message)

async def add_song_to_playlist(track_id):
    """
    Adds the specified Spotify track to the configured playlist.
    """
    logging.debug(f'Extracted track ID: {track_id}')
    try:
        track_uri = f'spotify:track:{track_id}'
        spotify.playlist_add_items(SPOTIFY_PLAYLIST_ID, [track_uri])
        logging.info(f'Added track {track_uri} to playlist.')
    except Exception as e:
        logging.error(f'Error adding track to playlist: {e}')

# Run the bot
bot.run(DISCORD_TOKEN)