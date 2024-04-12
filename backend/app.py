from collections import Counter, defaultdict
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__) # where we initialzed our app
# by default the flask run in production
# python-dotenv allow to create a flask dotenv file to have default info
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1001@localhost/Week-0-backend'
db = SQLAlchemy(app)
CORS(app)

class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(100), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"
    
    def __init__(self, description):
        self.description = description

with app.app_context():
    db.create_all()

class article_stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_count = db.Column(db.Integer, nullable=False)
    neutral_sentiment_count = db.Column(db.Integer, nullable=False)
    positive_sentiment_count = db.Column(db.Integer, nullable=False)
    negative_sentiment_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"ArticleStats: id={self.id}, article_count={self.article_count}, neutral_sentiment_count={self.neutral_sentiment_count}"

class source_articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"Channel_messages_ts: id={self.id}, channel_name={self.source_name}, text={self.content}, timestamp_events={self.timestamp}"

class article_sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    sentiment_text = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"article_sentiment: id={self.id}, channel={self.title}, text={self.content}, sentiment_score={self.sentiment_score}, sentiment={self.sentiment_text}"

@app.route('/article_stat', methods=['GET'])
def get_channel_activity():
    article_data = article_stat.query.all()
    article_list = []

    for article in article_data:
        article_list.append({
            "category": f"Category {article.category}",
            "title": article.title,  # Correct column name
            "content": article.content  # Correct column name
        })

    return jsonify({'channel_activity': article_list})

if __name__ == '__main__':
    app.run()