# For Google Gemini inference
import json
import os
from dotenv import load_dotenv
from google import genai

def generate_input_list(answers, user_keys):
    list_keys = [
        "occasion",
        "event_date",
        "location",
        "recipient_age",
        "relationship",
        "interests",
        "dislikes",
        "max_budget"
    ]
    input_list = []

    for key in list_keys:
        input_list.append(f"- {user_keys[key]}: {answers[key]}\n")

    return input_list

def generate_mock_prompt(answers):
    mock_prompt = f"""
    Example Prompt for Gift Generation Context: 
    You are a gift recommendation expert assistant. A user has filled out a form with the information below to find the perfect gift. Your task is to analyze the data and generate the best suggestions from the Shopee website (and only from the Shopee website), following the requested format.

    Data Collected from the User (Based on the Flow): 
    - Occasion: {answers["occasion"]}
    - Event Date: {answers["event_date"]}
    - Delivery Location: {answers["location"]}
    - Recipient Profile: Age: {answers["recipient_age"]}
    - Relationship with the user: {answers["relationship"]}
    - Interests and Hobbies: {answers["interests"]}
    - What they definitely dislike or already own: {answers["dislikes"]}
    - User Preferences: Maximum Budget: {answers["max_budget"]}

    Requested Response Format: Generate an output with a file JSON with Results according to the sessions below. Style: "Top 10 selections" (present the 10 best and most suitable options). Structure of each suggestion: Product Name URL Image Short and creative description (explaining why the gift is a good choice for the profile) Estimated Price Range (within the budget) Where to find: product link Task: Based on all the information above, go to Shopee and generate the Top 10 gift recommendations. Make sure the suggestions perfectly align with the interests ({{ $json.formData.interesses }}), respect the restrictions ({{ $json.formData.naoGosta }}) and the maximum budget of R$ {{ $json.formData.orcamento }}. Justify each choice creatively. Return only the list of products, formatted in pure JSON, without additional explanations. The JSON for each product must have the following structure: {{ "url": "product URL", "name": "product name", "image": "product image URL", "description": "product description", "price_range": "product price range", "where_to_find": "real link to the Shopee store" }}
    """

    return mock_prompt

def generate_prompt(answers):
    with open('app/text_data/en/prompt.json', 'r') as file:
        p = json.load(file)

    print(f"p --> {p}")

    prompt = generate_mock_prompt(answers)
    
    return prompt

def generate_gift_suggestions(answers):
    """Generate basic gift suggestions based on answers"""
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    client_prompt = generate_prompt(answers)

    print(f"\n\nclient_prompt:\n{client_prompt}\n\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=client_prompt,
        config={
            "tools": [{"google_search": {}}]
        }
    )

    print(f"response:\n{response.text}\n\n")

    return response.text