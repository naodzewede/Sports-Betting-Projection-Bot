# NBA Player Projection Discord Bot

## Overview
This Python project is a Discord bot developed to provide real-time NBA player projection updates. It utilizes the Discord API for communication, fetches data from an external source (Rotowire website) using HTTP requests, and handles and parses CSV data retrieved from the external source using the CSV module.

## Features
- Real-time NBA player projection updates.
- Fetching data from Rotowire website using HTTP requests.
- Parsing and handling CSV data for player projections.
- Discord bot functionality for interaction and dissemination of projections.

## Requirements
- Python 3.x
- discord.py library
- requests module
- CSV module

## Usage
1. Install the required dependencies:

2. Clone the repository or download the Python script.

3. Run the Python script.

4. Invite the bot to your Discord server using the provided OAuth link.

5. Interact with the bot using commands and receive NBA player projection updates.

## Commands
- `!instructions`: Display instructions on how to use the bot.
- Enter NBA player names and market names to receive their projections.

## How It Works
1. The bot fetches NBA player projection data from the Rotowire website.
2. Upon receiving a message containing a player's name and market name, it retrieves the corresponding projection from the CSV data.
3. The bot then categorizes the projection based on risk level and sends the projection along with a breakdown of projection factors to the Discord channel.

## Discord Bot Token
To run the bot, replace the `client.run()` method with your Discord bot token.

## Disclaimer
This bot provides projections based on available data and factors, but actual player performance may vary. It's intended for informational purposes only.
