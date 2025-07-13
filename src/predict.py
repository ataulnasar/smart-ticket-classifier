import joblib
import sys

# Load trained model
model = joblib.load('model/ticket_classifier.pkl')

def predict_category(text: str) -> str:
    prediction = model.predict([text])[0]
    return prediction

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py \"Your ticket text here\"")
    else:
        input_text = " ".join(sys.argv[1:])
        category = predict_category(input_text)
        print(f"Predicted Category: {category}")
