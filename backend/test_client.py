import requests
import json

BASE_URL = 'http://localhost:5000/api'

def test_api():
    # 1)
    # Test getting questions
    print("Testing questions endpoint...")
    response = requests.get(f'{BASE_URL}/questions')
    if response.status_code == 200:
        print("Questions endpoint working.\n")
        print("Question endpoint status :\n")
        print(response)
        # for q in response.json():
        #     print(f"{q['id']}. {q['question']}\n")
    else:
        print("Questions endpoint failed")
        return
    
    # 2)
    # Test submitting a recommendation
    print("\nTesting submission endpoint")

    # Sample data for testing
    # sample_data = {
    #     "occasion": "Birthday",
    #     "event_date": "2024-12-25",
    #     "location": "New York",
    #     "recipient_age": 30,
    #     "relationship": "Friend",
    #     "interests": ["Reading", "Hiking", "Coffee", "Technology"],
    #     "dislikes": ["Chocolate", "Scented candles"],
    #     "max_budget": 100.0,
    #     "country": "BR",
    #     "language": "en"
    # }
    sample_data = {
        "occasion": "Anniversary",
        "event_date": "2026-03-17",
        "location": "Belo Horizonte, MG, Brazil",
        "recipient_age": 39,
        "relationship": "Girlfriend",
        "interests": ["Style", "Anime", "Music"],
        "dislikes": ["Olives", "Grapes"],
        "max_budget": 500.0,
        "country": "BR",
        "language": "en"
    }

    # Submit answers
    response = requests.post(f'{BASE_URL}/submit', 
        json=sample_data,
        headers={'Content-Type': 'application/json'})
    
    if response.status_code == 201:
        print("Successfully submitted answers!")
        result = response.json()
        recommendation_id = result['id']
        print(f"Recommendation ID: {recommendation_id}")

        #Test getting specific recommendation
        print("\nTesting single recommendation endpoint...")
        response = requests.get(f'{BASE_URL}/recommendations/{recommendation_id}')

        if response.status_code == 200:
            print(f"Response: \n {response.json()}\n")
            print("Single recommendation endpoint working")
        else:
            print("Single recommendation endpoint failed")

        # Test generating suggestions
        print("\nTesting suggestions endpoint...")
        response = requests.get(f'{BASE_URL}/generate-suggestions/{recommendation_id}')
        
        if response.status_code == 200:
            # print(f"TODO: rm me!\n {response.json()}")
            suggestions = response.json()['suggestions']
            print(f"Suggestions generated: {len(suggestions)} items\n\n")

            print(f"Suggestions ->\n{suggestions}\n\n")
        else:
            print(f"Suggestions endpoint failed {response.json()}")
    else:
        prettified_res = json.dumps(response.json(), indent=2, ensure_ascii=False)
        print(f"Submission failed: {prettified_res}")

    # Test getting all recommendations
    print("\nTesting all recommendations endpoint...")
    response = requests.get(f'{BASE_URL}/recommendations')

    if response.status_code == 200:
        recommendations = response.json()
        print(f"All recommendations endpoint working. Total: {len(recommendations)}")
    else:
        print("All recommendations endpoint failed")


if __name__ == '__main__':
    test_api()