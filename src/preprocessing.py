import pandas as pd
import random

# Sample categories and phrases
categories = ["Billing", "Technical Issue", "Account Management", "Feature Request", "General Inquiry"]

ticket_templates = {
    "Billing": [
        "I was charged twice for my subscription.",
        "Why is my invoice amount higher this month?",
        "Can you explain this charge on my credit card?",
        "I need a refund for a mistaken payment.",
        "My billing history is missing from the dashboard."
    ],
    "Technical Issue": [
        "The app crashes every time I open it.",
        "I can't log into my account.",
        "The search function isn't working properly.",
        "I'm getting an error when uploading files.",
        "The website loads very slowly on my computer."
    ],
    "Account Management": [
        "How do I reset my password?",
        "I want to update my email address.",
        "Please delete my account permanently.",
        "How can I change my username?",
        "I need to merge two of my accounts."
    ],
    "Feature Request": [
        "Can you add dark mode support?",
        "It would be great to have a mobile app.",
        "Please consider integrating with Google Calendar.",
        "Can you allow exporting data to Excel?",
        "I’d love a notification system for updates."
    ],
    "General Inquiry": [
        "What are your support hours?",
        "Do you offer discounts for students?",
        "Where are your servers located?",
        "Is my data encrypted?",
        "What is your privacy policy?"
    ]
}

# Generate 1000 tickets
random.seed(42)
data = []
for _ in range(1000):
    category = random.choice(categories)
    text = random.choice(ticket_templates[category])
    data.append({"text": text, "category": category})

df = pd.DataFrame(data)

# Save to CSV
csv_path = "/mnt/data/support_tickets.csv"
df.to_csv(csv_path, index=False)

csv_path