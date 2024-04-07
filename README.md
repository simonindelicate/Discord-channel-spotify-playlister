# Discord Spotify Playlist Bot

This is a Discord bot that listens for Spotify track links in a specific channel and automatically adds them to a predefined Spotify playlist.

## Features

- Listens for Spotify track links in the "music-recommendations" channel.
- Automatically adds the tracks to a specified Spotify playlist.
- Responds with a random message when the bot is mentioned.

## Prerequisites

- Python 3.6 or higher.
- Discord Bot Token.
- Spotify Developer Credentials (Client ID, Client Secret, Redirect URI).
- Spotify Playlist ID.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/discord-spotify-playlist-bot.git
    cd discord-spotify-playlist-bot
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up the Discord Bot:
    - Create a new Discord application on the Discord Developer Portal.
    - Create a bot and copy the bot token.
    - Invite the bot to your Discord server.

4. Set up the Spotify Developer credentials:
    - Create a new Spotify Developer application on the Spotify Developer Dashboard.
    - Copy the Client ID, Client Secret, and Redirect URI.
    - Create a new Spotify playlist and copy the playlist ID.

5. Configure the bot:
    - Open the `main.py` file.
    - Replace the placeholders with your own Discord bot token, Spotify credentials, and playlist ID:
        ```python
        # Discord Bot Token
        DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

        # Spotify Credentials
        SPOTIFY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
        SPOTIFY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
        SPOTIFY_REDIRECT_URI = 'YOUR_SPOTIFY_REDIRECT_URI'
        SPOTIFY_PLAYLIST_ID = 'YOUR_SPOTIFY_PLAYLIST_ID'
        ```
    - (Optional) Customize the `mention_replies` list with your own responses.

6. Run the bot:
    ```bash
    python main.py
    ```
    The bot will start running and display a message in the console with the URL to authorize the Spotify integration. Follow the instructions to complete the authorization process.

## Usage

- Invite the bot to your Discord server and make sure it has the necessary permissions (e.g., "Send Messages" and "Read Message History").
- In your Discord server, create a text channel named "music-recommendations".
- Whenever someone posts a Spotify track link in the "music-recommendations" channel, the bot will automatically add the track to the specified Spotify playlist.
- If the bot is mentioned in any channel (except when it's mentioned by everyone), it will respond with a random message from the `mention_replies` list.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
