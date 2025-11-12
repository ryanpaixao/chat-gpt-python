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

def generate_prompt(answers):
    with open('../text_data/en/prompt.json', 'r') as file:
        p = json.load(file)

    p_list = [p.gift_generation_context, p.data_collected_from_user.data_collected, "\n"]
    user_input = generate_input_list(answers, p.data_collected_from_user)
    p_list.append(user_input)
    p_list.extend(p.requested_response_format)
    p_list.extend([p.user_alignments.alignment[0], answers.interests])
    p_list.extend([p.user_alignments.restrictions[0], answers.dislikes])
    p_list.extend([p.user_alignments.max_budget[0], answers.max_budget])
    p_list.extend(p.user_alignments.justify)

    prompt = " ".join(p_list)
    
    return prompt

def generate_gift_suggestions(answers):
    """Generate basic gift suggestions based on answers"""
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    client_prompt = generate_prompt(answers)

    print(f"client_prompt:\n{client_prompt}\n\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=client_prompt
    )

    return response