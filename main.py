from flask import Flask, request, jsonify
from flask_cors import CORS
from src.LLM import generate, init

db, text_model = init()

port_no = 5000

app = Flask(__name__)
CORS(app)


@app.route("/ask", methods=["GET", "POST"])
def generate_response():
    if request.method == "GET":
        return "Please send POST request"

    elif request.method == "POST":
        query = request.json["query"]

        response, passage = generate(text_model, query, db)

        data = {"Response": response, "Context": passage}

        return jsonify(data)


print("Server running....")

app.run(port=port_no)
