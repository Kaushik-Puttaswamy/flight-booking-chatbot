from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/book', methods=['POST'])
def book_flight():
    data = request.get_json()
    origin = data.get('origin')
    destination = data.get('destination')
    date = data.get('date')

    if origin and destination and date:
        return jsonify({"status": "success", "message": "Flight booked!"})
    else:
        return jsonify({"status": "error", "message": "Missing data"}), 400

if __name__ == "__main__":
    app.run(port=5000)