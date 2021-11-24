from flask import Flask
from datetime import datetime
app=Flask(__name__)#本地端

#建立router
@app.route('/')
def index():
    return 'Hello!,Calvin'

@app.route('/today')
def today():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S ')


app.run(debug=True)
