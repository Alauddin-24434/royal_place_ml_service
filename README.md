# Royal Place Resort ML Service

This ML service is designed to enhance the guest experience at the Royal Place Resort. It uses machine learning models to analyze guest reviews, provide personalized recommendations, enable smart room selection, and offer dynamic discounts.

## 🚀 Features

  - **Sentiment Analysis:** Analyzes guest reviews to understand their sentiment (positive, negative, neutral). (`review_analyzer.py`)
  - **Dynamic Discounts:** Automatically generates discount offers for guests by analyzing booking data and other factors. (`discount_model.py`)
  - **Personalized Recommendations:** Recommends personalized services or amenities based on guest preferences and past activities. (`recommender.py`)
  - **Smart Room Selection:** Suggests the most suitable room type based on guest needs and the resort's current availability. (`room_selector.py`)

## 🛠️ Installation

Follow these steps to set up the project:

1.  Clone the project repository:
    ```bash
    git clone <repo_url>
    cd ml_service
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    ```
      - **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
      - **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
3.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ How to Run

To run the project, use the following command:

```bash
uvicorn ml_service_main:app --reload --port 8000
```

This will start your API server at `http://127.0.0.1:8000`.

## 💻 API Endpoints

The main API endpoints available for your service are listed below. All endpoints use the `POST` method.

  - **`/ml/sentiment`**
      - **Description:** Analyzes the sentiment of a guest review.
      - **Request Body Example:**
        ```json
        {
          "review_text": "The service was excellent and the staff were very helpful."
        }
        ```
  - **`/ml/recommend`**
      - **Description:** Provides personalized recommendations for a guest.
      - **Request Body Example:**
        ```json
        {
          "guest_id": "guest_123"
        }
        ```
  - **`/ml/room-suggest`**
      - **Description:** Suggests a suitable room type based on guest information.
      - **Request Body Example:**
        ```json
        {
          "number_of_guests": 2,
          "stay_duration_days": 3
        }
        ```
  - **`/ml/discount`**
      - **Description:** Checks for discount eligibility and suggests potential discounts.
      - **Request Body Example:**
        ```json
        {
          "booking_date": "2025-10-25",
          "guest_tier": "gold"
        }
        ```

-----

Now that you have your core `README.md` file, would you like me to help you draft a `CONTRIBUTING.md` file with guidelines for potential contributors or a `CHANGELOG.md` to track your project's version history?