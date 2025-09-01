from fastapi import FastAPI
from pydantic import BaseModel
from review_analyzer import sentiment_analyzer_function
from discount_model import discount_function
from recommender import recommend_services
from room_selector import predict_room


app = FastAPI(title="Royal Palace Resort ML Service")

# ---------- Request Models ----------
class Review(BaseModel):
    text: str

class GuestBooking(BaseModel):
    guest_id: str
    bookings_count: int

class GuestHistory(BaseModel):
    guest_id: str

class RoomRequest(BaseModel):
    guest_type: str
    family_size: int
    purpose: str

# ---------- Sentiment Analysis ----------
@app.post("/sentiment")
def analyze_sentiment(review: Review):
    return sentiment_analyzer_function(review.text)

# ---------- Dynamic Discounts ----------
@app.post("/discount")
def get_discount(booking: GuestBooking):
    return discount_function(booking.guest_id, booking.bookings_count)

# ---------- Personalized Recommendation ----------
@app.post("/recommend")
def recommend(history: GuestHistory):
    return recommend_services(history.guest_id)

# ---------- Smart Room Selection ----------
@app.post("/room-suggest")
def room_suggest(request: RoomRequest):
    return predict_room(request.guest_type, request.family_size, request.purpose)

# ---------- Root ----------
@app.get("/")
def root():
    return {"message": "Royal Palace Resort ML Service is running!"}
