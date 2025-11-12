from flask import Blueprint, jsonify
import json

bp = Blueprint('questions', __name__)

# Read JSON question file
with open('../text_data/en/questions.json', 'r') as file:
    questions = json.load(file)

@bp.route('/api/questions', methods=['GET'])
def get_questions():
    """Endpoint to get all questions"""
    return jsonify(questions)