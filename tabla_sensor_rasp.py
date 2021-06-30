from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('table.html')

@app.route('/hello.html')  # crea la ruta del servidor creado
def hello():
    return 'Hello, World!'


@app.route('/get_data.json')  # crea la ruta del servidor creado
def get_data():
    response = {"data": []}
    with open('/home/pi/datos.csv') as fin:
        data = fin.readline()

        text_td = " "
        #print (data)
        for line in fin:
            temp, pres, hum,time = line.rstrip('\n').split(",")
            response['data'].append([temp, pres, hum, time])

        jsonStr = json.dumps(response)
        return jsonStr


if __name__ == '__main__':
    app.run(host="0.0.0.0")
