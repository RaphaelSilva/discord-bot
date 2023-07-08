import argparse
import sys
import dbot.app as app
import os

TOKEN = os.getenv('DISCORD_TOKEN')

parser = argparse.ArgumentParser(description="Choese the service to up")
parser.add_argument("--start",
                     choices=['client', 'command'], 
                     required=True, 
                     help='[client] to start the SendVideoToYoutubeCliente OR [command] to start the SendVideoToYoutubeCommand')
action = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    app.init(action.start)(TOKEN)