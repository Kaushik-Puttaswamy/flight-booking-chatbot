from typing import Any, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionBookFlight(Action):
    def name(self) -> str:
        return "action_book_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        origin = tracker.get_slot("origin")
        destination = tracker.get_slot("destination")
        date = tracker.get_slot("date")

        if not all([origin, destination, date]):
            dispatcher.utter_message(text="Missing some information to book your flight.")
            return []

        payload = {
            "origin": origin,
            "destination": destination,
            "date": date
        }

        try:
            response = requests.post("http://localhost:5000/book", json=payload)
            data = response.json()

            if data.get("status") == "success":
                dispatcher.utter_message(text=f"Your flight from {origin} to {destination} on {date} has been booked.")
            else:
                dispatcher.utter_message(text="Something went wrong with the booking.")
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to book flight: {e}")

        return []