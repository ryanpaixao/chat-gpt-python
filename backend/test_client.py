import requests
import json

BASE_URL = 'http://localhost:5000/api'

def test_api():
    # Get questions
    response = requests.get(f'{BASE_URL}/questions')
    print("Available questions:")
    for q in response.json():
        print(f"{q['id']}. {q['question']}")
    print("\n")

    # Sample data for testing
    sample_data = {
        "occasion": "Birthday",
        "event_date": "2024-12-25",
        "location": "New York",
        "recipient_age": 30,
        "relationship": "Friend",
        "interests": "Reading, Hiking, Coffee, Technology",
        "dislikes": "Chocolate, Scented candles",
        "max_budget": 100.0
    }

    # Submit answers
    response = requests.post(f'{BASE_URL}/submit', 
        json=sample_data,
        headers={'Content-Type': 'application/json'})
    
    if response.status_code == 201:
        print("Successfully submitted answers!")
        result = response.json()
        print(f"Recommendation ID: {result['id']}")
    else:
        print(f"Error: {response.json()}")

    # Get all recommendations
    print("\nAll stored recommendations:")
    response = requests.get(f'{BASE_URL}/recommendations')
    recommendations = response.json()
    for rec in recommendations:
        print(f"ID: {rec['id']}, Occasion: {rec['occasion']}, Budget: ${rec['max_budget']}")

if __name__ == '__main__':
    test_api()