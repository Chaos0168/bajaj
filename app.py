from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route("/bfhl", methods=["POST"])
def process_data():
    try:
        data = request.get_json()
        if "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid JSON format"}), 400

        user_id = "TriptSachdeva_16102004"  
        email = "22bcs15007@cuchd.in"  
        roll_number = "22BCS15007"  

        numbers = [x for x in data["data"] if x.isdigit()]
        alphabets = [x for x in data["data"] if x.isalpha()]

        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route("/bfhl", methods=["GET"])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == "__main__":
    app.run(debug=True)
