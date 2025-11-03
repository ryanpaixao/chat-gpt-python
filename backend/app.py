from flask import Flask, request, jsonify
from models import db, GiftRecommendation
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gift_recommendations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/api/questions', methods=['GET'])
def get_questions():
    """Endpoint to get all questions"""
    questions = [
        {
            'id': 1,
            'question': "What's the occasion?",
            'field_name': 'occasion',
            'type': 'text',
            'placeholder': 'e.g., Birthday, Anniversary, Christmas'
        },
        {
            'id': 2,
            'question': "When is the Event Date?",
            'field_name': 'event_date',
            'type': 'date',
            'placeholder': 'YYYY-MM-DD'
        },
        {
            'id': 3,
            'question': "What is the location of the recipient?",
            'field_name': 'location',
            'type': 'text',
            'placeholder': 'e.g., New York, USA'
        },
        {
            'id': 4,
            'question': "How old is the recipient?",
            'field_name': 'recipient_age',
            'type': 'number',
            'placeholder': 'Enter age'
        },
        {
            'id': 5,
            'question': "What's your relationship with the recipient?",
            'field_name': 'relationship',
            'type': 'text',
            'placeholder': 'e.g., Friend, Family, Colleague'
        },
        {
            'id': 6,
            'question': "What are the recipient's interests and hobbies?",
            'field_name': 'interests',
            'type': 'array',
            'placeholder': 'Add interests one by one',
            'description': 'Press Enter after each interest to add it to the list'
        },
        {
            'id': 7,
            'question': "What does the recipient dislike or already own?",
            'field_name': 'dislikes',
            'type': 'array',
            'placeholder': 'Add dislikes one by one',
            'description': 'Press Enter after each item to add it to the list'
        },
        {
            'id': 8,
            'question': "What's your maximum budget?",
            'field_name': 'max_budget',
            'type': 'number',
            'placeholder': 'Enter amount in R$'
        }
    ]
    return jsonify(questions)

@app.route('/api/submit', methods=['POST'])
def submit_answers():
    """Endpoint to submit all answers"""
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = [ 'occasion', 'event_date', 'location', 'recipient_age', 'relationship', 'interests', 'dislikes', 'max_budget']

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
            interests=data['interests'],
            dislikes=data['dislikes'],
            max_budget=data['max_budget']
        )

        # Set interests and dislikes using array -> JSON methods
        recommendation.set_interests(data['interests'])
        recommendation.set_dislikes(data['dislikes'])

        db.session.add(recommendation)
        db.session.commit()

        return jsonify({
            'message': 'Recommendation saved successfully!',
            'id': recommendation.id,
            'data': recommendation.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    """Endpoint to get all stored recommendations"""
    recommendations = GiftRecommendation.query.all()
    return jsonify([rec.to_dict() for rec in recommendations])

@app.route('/api/recommendations/<int:id>', methods=['GET'])
def get_recommendation(id):
    """Endpoint to get a specific recommendation"""
    recommendation = GiftRecommendation.query.get_or_404(id)
    return jsonify(recommendation.to_dict())

if __name__ == '__main__':
    app.run(debug=True, port=5000)