from flask import Flask, request, jsonify
from flask_cors import CORS
from src.LLM import generate, init

db = init()

port_no = 10000

app = Flask(__name__)
CORS(app)


@app.route("/ask", methods=["GET", "POST"])
def generate_response():
    if request.method == "GET":
        return "Please send POST request"

    elif request.method == "POST":
        query = request.json["query"]

        response, passage = generate(query, db)

        data = {"Response": response, "Context": passage}

        return jsonify(data)


print("Server running....")

app.run(port=port_no)
