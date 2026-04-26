from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify({
        "message": "Step 5 API working",
        "name": "Afreen"
    })

if __name__ == '__main__':
    app.run(debug=True)