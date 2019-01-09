"""
This script runs the Master application using a development server.
"""

from os import environ
from Master import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = 80
    app.run(HOST, PORT)
