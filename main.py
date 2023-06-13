import json
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    print("running")
    print("running")
    return json.dumps(players)

@app.route('/api')
def api():
    print("running")
app.run()