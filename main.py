import socket

from back.camera import click
from back.master_photo import go
from back.return_one import apdate


import eel
my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': socket.gethostbyname(socket.gethostname()),
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}



if __name__ == '__main__':
    
    print(socket.gethostbyname(socket.gethostname()))
    eel.init('front')
    eel.start('index.html', options=my_options,suppress_error=True)
    



