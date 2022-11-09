from flask import Flask,jsonify,request,render_template
import pickle
import json
app=Flask(__name__)
with open('Autos_model.pkl','rb')as f:
    model=pickle.load(f)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=["POST"])
def predict():
    array=[float(x) for x in request.form.values()]
    pred=model.predict([array])[0]
    return render_template('home.html',prediction_text=f"Predicted price of your car is {pred} $")


if __name__=="__main__":
   app.run(debug=True)