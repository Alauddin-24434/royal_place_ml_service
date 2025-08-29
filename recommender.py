# Simple demo recommendation
# In real: use Surprise library or other collaborative filtering

guest_service_history = {
    "guest1": ["Spa", "Gym", "Pool"],
    "guest2": ["Restaurant", "Bar"],
    "guest3": ["Gym", "Pool"]
}

def recommend_services(guest_id: str):
    services = guest_service_history.get(guest_id, ["Restaurant", "Spa"])
    return {"feature": "recommendation", "guest_id": guest_id, "recommended_services": services}
