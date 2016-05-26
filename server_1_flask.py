from flask import Flask, jsonify
import time
app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name='Anonymous'):
    time.sleep(2)
    return jsonify({
        'hello': name,
    })

app.run(port=8080)
