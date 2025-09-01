def discount_function(guest_id: str, bookings_count: int):
    """
    Simple rule-based discount:
    ≥3 bookings → 10% discount
    """
    discount = 0
    if bookings_count >= 3:
        discount = 10
    return {"feature": "discount", "guest_id": guest_id, "discount": discount}
