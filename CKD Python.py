from flask import Flask,render_template,request
import pickle
 app = Flask(__name__)
mopdel = pickle.load(open('CKD.pkl','rb'))
@app.route('/')
def home():
  return render_template(home.html)
@app.route('/prediction',methods=['POST','GET'])
 
def prediction():
   return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_home();
   return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
     input_features = [float9x0 for x in request.form.values.form.values()]
     features_value = [np.array(input_features)]

features_name = ['blood_urea','blood glucose random','anemia','coronary_artery_disease',
                                'pus_cell','red_blood_cells','diabetesmellitus','pedal_edema']

df = pd.DataFrame(features_value,columns=features_name)

output = model.predict(df)

return render_template('result.html',prediction_text=output)

if__name__ == '__main__':
app.run(debug=True)

