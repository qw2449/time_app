from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

# Newly added to show time
@app.route('/time')
def show_time():
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return time_str

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
