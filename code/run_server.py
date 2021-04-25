from app import app, Server
import os

server = Server(app)
server.config()
server.run()

if __name__ == '__main__':
    os.environ['APP_GITHUB_TOKEN'] = ''
    app.run()
