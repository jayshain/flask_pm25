from flask import Flask,render_template
from datetime import datetime
app=Flask(__name__)#本地端

#建立router
@app.route('/')
def index():
    name = 'Calvin'
    time=today()
    return render_template('index.html', **locals())

@app.route('/today')
def today():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S ')


app.run(debug=True)
