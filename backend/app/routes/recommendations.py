from flask import Blueprint, request, jsonify
from app.models import GiftRecommendation, db
from datetime import datetime

bp = Blueprint('recommendations', __name__)

@bp.route('/api/submit', methods=['POST'])
def submit_answers():
    """Endpoint to submit all answers"""
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = [
            'occasion',
            'event_date',
            'location',
            'recipient_age',
            'relationship',
            'interests',
            'dislikes',
            'max_budget'
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
            
        # Validate that interests and dislikes are arrays
        if not isinstance(data['interests'], list):
            return jsonify({'error': 'Interests must be an array'}), 400
        if not isinstance(data['dislikes'], list):
            return jsonify({'error': 'Dislikes must be an array'}), 400
        
        # Create new recommendation
        recommendation = GiftRecommendation(
            occasion=data['occasion'],
            event_date=datetime.strptime(data['event_date'], '%Y-%m-%d').date(),
            location=data['location'],
            recipient_age=data['recipient_age'],
            relationship=data['relationship'],
            max_budget=data['max_budget']
        )

        # Set interests and dislikes using the new methods
        recommendation.set_interests(data['interests'])
        recommendation.set_dislikes(data['dislikes'])

        db.session.add(recommendation)
        db.session.commit()

        return jsonify({
            'message': 'Recommendation saved successfully!',
            'id': recommendation.id,
            'data': recommendation.to_dict()
        }), 201
    
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': f'Invalid date format. Use YYYY-MM-DD.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@bp.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    """Endpoint to get all stored recommendations"""
    try:
        recommendations = GiftRecommendation.query.all()
        return jsonify([rec.to_dict() for rec in recommendations])
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@bp.route('/api/recommendations/<string:id>', methods=['GET'])
def get_recommendation(id):
    """Endpoint to get a specific recommendation by UUID"""
    try:
        recommendation = GiftRecommendation.query.get_or_404(id)
        return jsonify(recommendation.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 404