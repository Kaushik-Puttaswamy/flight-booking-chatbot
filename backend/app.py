from flask import Flask, request, jsonify
from mock_flights import find_flights
from database import save_booking

app = Flask(__name__)

@app.route('/book', methods=['POST'])
def book_flight():
    data = request.json
    origin = data.get("origin")
    destination = data.get("destination")
    date = data.get("date")

    if not origin or not destination or not date:
        return jsonify({"status": "error", "message": "Missing data"}), 400

    # Simulate flight lookup
    flight = find_flights(origin, destination, date)

    if not flight:
        return jsonify({"status": "error", "message": "No flights found"}), 404

    # Save the booking
    save_booking(origin, destination, date)

    return jsonify({
        "status": "success",
        "flight": flight
    })