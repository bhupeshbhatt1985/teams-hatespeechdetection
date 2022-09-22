import numpy as np
from flask import Flask, request, jsonify, render_template, session
import pickle



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def home():
    session['pt']=""
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.pop('pt')
    session['pt']=""
    return render_template('index.html')
    



@app.route('/predict',methods=['POST'])
def predict():
    hate_words = [x for x in request.form.values()]
    text = hate_words
    hate_words = [hate_words[0].lower()]
    print("hate_words")
    print(hate_words)
    lr = pickle.load(open('lr.pickel', 'rb'))
    cv = pickle.load(open('cv.pickel', 'rb'))

    #lr = pickle.load(open('HateSpeechDetection.pkl', 'rb'))
    #cv = pickle.load(open('vectorizer.pkl', 'rb'))

    # transform documents to document-term matrix
    x_sample_vec = cv.transform(hate_words).toarray()
    print(x_sample_vec)
    
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    prediction = lr.predict(x_sample_vec)

    #prediction_text = "Not Hate Speech"
    pt =  session["pt"] 
    print("prediction")
    print(prediction)
    if(prediction[0] == 0):
        pt = pt + "<p class='notblocked'>"+ text[0] +"</p>"
    else:
        pt = pt + "<p class='blocked'>hate speech detected and deleted !!</p>"
    
    session["pt"] = pt
    return render_template('index.html', prediction_text=pt)


if __name__ == "__main__":
    app.run(debug=True)