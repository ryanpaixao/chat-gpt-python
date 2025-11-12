from app import db
from datetime import datetime
import json
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class GiftRecommendation(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    occasion = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    recipient_age = db.Column(db.Integer, nullable=False)
    relationship = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.Text, nullable=False)
    dislikes = db.Column(db.Text, nullable=False)
    max_budget = db.Column(db.Float, nullable=False)
    created_at = db. Column(db.DateTime, default=datetime.utcnow)

    def set_interests(self, interests_list):
        """Convert list to JSON string for storage"""
        self.interests = json.dumps(interests_list)

    def get_interests(self):
        """Convert JSON string back to list"""
        return json.loads(self.interests) if self.interests else []
    
    def set_dislikes(self, dislikes_list):
        """Convert list to JSON string for storage"""
        self.dislikes = json.dumps(dislikes_list)

    def get_dislikes(self):
        """Convert JSON string back to list"""
        return json.loads(self.dislikes) if self.dislikes else []

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