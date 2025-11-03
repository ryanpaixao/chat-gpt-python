from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class GiftRecommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    occasion = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    recipient_age = db.Column(db.Integer, nullable=False)
    relationship = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.Text, nullable=False)
    dislikes = db.Column(db.Text, nullable=False)
    max_budget = db.Column(db.Float, nullable=False)
    created_at = db. Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'occasion': self.occasion,
            'event_date': self.event_date.isoformat(),
            'location': self.location,
            'recipient_age': self.recipient_age,
            'relationship': self.relationship,
            'interests': self.interests,
            'dislikes': self.dislikes,
            'max_budget': self.max_budget,
            'created_at': self.created_at.isoformat()
        }