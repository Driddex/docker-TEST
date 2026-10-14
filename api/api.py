from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/p', methods=["POST"])
def p():
    data = request.get_json() or {}
    user_id = data.get("id")

    return jsonify({"received_id": user_id})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)