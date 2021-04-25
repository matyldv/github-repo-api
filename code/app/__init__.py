from flask import Flask
from app.server import Server
from app.user import UserInfo
from app.info import GetInfo

app = Flask(__name__)
from app import routes
