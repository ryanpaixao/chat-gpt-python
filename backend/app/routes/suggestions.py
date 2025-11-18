from flask import Blueprint, jsonify
from app.models import GiftRecommendation
from utils.gift_suggestions import generate_gift_suggestions

bp = Blueprint('suggestions', __name__)

@bp.route('/api/generate-suggestions/<string:id>', methods=['GET'])
def generate_suggestions(id):
    """Generate gift suggestions using AI service"""
    try:
        recommendation = GiftRecommendation.query.get_or_404(id).to_dict()

        answers = {
            'occasion': recommendation["occasion"],
            'event_date': recommendation["event_date"],
            'location': recommendation["location"],
            'recipient_age': recommendation["recipient_age"],
            'relationship': recommendation["relationship"],
            'interests': recommendation["interests"],
            'dislikes': recommendation["dislikes"],
            'max_budget': recommendation["max_budget"],
        }

        suggestions = generate_gift_suggestions(answers)

        return jsonify({
            'recommendation': recommendation,
            'suggestions': suggestions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 404