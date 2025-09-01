# Simple demo: rule-based room selection
def predict_room(guest_type: str, family_size: int, purpose: str):
    if family_size >= 4:
        room = "Family Suite"
    elif purpose.lower() == "business":
        room = "Business Room"
    else:
        room = "Standard Room"
    return {"feature": "room_selection", "suggested_room": room}
