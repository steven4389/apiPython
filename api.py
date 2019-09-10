from flask import Flask
from flask_cors import CORS, cross_origin
from numpy.random import randint
from numpy.random import rand
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test_json():
 x_edades = randint(18,57,100).tolist()
#  x_edades = json.dumps(x_edades)

 y_edades = randint(18,57,100).tolist()
#  y_edades = json.dumps(x_edades)
 
 list = [
            y_edades,
            x_edades
        ]
 
 return json.dumps(list)
    
    

app.run(debug= False, port=8000)