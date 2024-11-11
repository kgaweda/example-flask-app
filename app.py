from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def helloApi():
    data = {
        "name": "Hello world"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)