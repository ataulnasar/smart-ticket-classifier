from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model
model = joblib.load("model/ticket_classifier.pkl")

# Define request body
class Ticket(BaseModel):
    text: str

# Initialize app
app = FastAPI(title="Support Ticket Classifier API")

@app.get("/")
def read_root():
    return {"message": "Support Ticket Classifier is running!"}

@app.post("/predict")
def predict(ticket: Ticket):
    category = model.predict([ticket.text])[0]
    return {"predicted_category": category}
