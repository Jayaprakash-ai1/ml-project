from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 
@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        Date= request.form.get('Date')
        Store = request.form.get('Store')
        Item = request.form.get('Item')
          

    prediction = utils.preprocessdata(Date,Store,Item)
    print(prediction)
    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__': 
    app.run(debug=True) 
