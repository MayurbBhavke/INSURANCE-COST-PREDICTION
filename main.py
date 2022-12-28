from flask import Flask , render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('Inusrance-cost-prediction.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        children = int(request.form['children'])
        bmi = float(request.form['bmi'])
        sex = request.form['sex']
        if(sex == 'male'):
            sex=1
        else:
            sex=0

        smoker=request.form['smoker']
        if(smoker=='yes'):
            smoker=1
        else:
            smoker=0

        prediction=model.predict([[age , sex , bmi , children ,smoker ]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',pred="Sorry you cannot sell this car")
        else:
            pred = "For the person with age  {} , {} children, {} bmi, {} sex, {} smoker , Your Insurance cost price is {}".format(age, children, bmi, sex, smoker, output)
            return render_template('index.html',pred=pred)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

