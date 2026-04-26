from flask import Flask, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict/<int:value>')
def predict(value):
    result = model.predict([[value]])
    return jsonify({"prediction": result.tolist()})

if __name__ == '__main__':
    app.run(debug=True)