from flask import Flask,render_template
from datetime import datetime
import pandas as pd

app=Flask(__name__)#本地端

#建立router
@app.route('/pm25')
def pm25():
    url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
    df = pd.read_csv(url)[['county','Site','PM25','ItemUnit']]
    columns=df.columns
    values=df.values.tolist()
    time = today()

    return render_template('pm25.html', **locals())



@app.route('/')
def index():
    name = 'Calvin'
    time=today()
    return render_template('index.html', **locals())

@app.route('/today')
def today():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S ')


app.run(debug=True)
