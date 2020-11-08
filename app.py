import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")
    # return hello 
    
@app.route("/predict", methods = ["POST"])

def predict():
    #takes the html input
    int_feature = [int(x) for x in request.form.values()]
    # make it an array
    final_feature = [np.array(int_feature)]
    
    prediction = model.predict(final_feature)
    
    output = round(prediction[0], 2)
    
    #return the template to the html
    return render_template("index.html", prediction_text = "well hello = {}".format(output))


# run the app
if __name__ == "__main__":
    app.run(debug = True)