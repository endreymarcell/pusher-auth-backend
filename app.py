import json
import os
import sys

from flask import Flask, request
from flask_cors import CORS
import pusher

if not ('PUSHER_APP_ID' in os.environ and 'PUSHER_KEY' in os.environ and 'PUSHER_SECRET' in os.environ):
  print 'Please specify the PUSHER_APP_ID, PUSHER_KEY, and PUSHER_SECRET environmental variables'
  sys.exit(1)

app = Flask(__name__)
CORS(app)

pusher_client = pusher.Pusher(
  app_id=os.environ['PUSHER_APP_ID'],
  key=os.environ['PUSHER_KEY'],
  secret=os.environ['PUSHER_SECRET'],
  cluster='eu',
  ssl=True
)

@app.route("/", methods=['GET'])
def index():
  return 'POST to /pusher/auth/'

@app.route("/pusher/auth/", methods=['POST'])
def pusher_authentication():
  auth = pusher_client.authenticate(
    channel=request.form['channel_name'],
    socket_id=request.form['socket_id']
  )
  return json.dumps(auth)
