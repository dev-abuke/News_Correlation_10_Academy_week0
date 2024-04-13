from collections import Counter, defaultdict
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy import cast, Date
import time

app = Flask(__name__) # where we initialzed our app
# by default the flask run in production
# python-dotenv allow to create a flask dotenv file to have default info
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:hello@localhost:5434/newsdb'
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

# class articles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     url = db.Column(db.String, nullable=False)
#     category = db.Column(db.String, nullable=False)
#     content = db.Column(db.String, nullable=False)
#     source = db.Column(db.String, nullable=False)
#     sentiment = db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return f"ArticleStats: id={self.id}, title={self.title}, url={self.url}"

class articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String, nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    date_published = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Channel_messages_ts: id={self.id}, channel_name={self.source}, text={self.sentiment_score}"

class article_sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    sentiment_text = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"article_sentiment: id={self.id}, channel={self.title}, text={self.content}, sentiment_score={self.sentiment_score}, sentiment={self.sentiment_text}"

@app.route('/sentiment_stat', methods=['GET'])
def get_sentiment():
    
    articles_db = articles.query.filter(articles.source.isnot(None)).all()
    
    sentiment_data = [(article.source, article.sentiment_score) for article in articles_db]
    # Extract all sentiment scores
    sentiment_scores = [score for _, score in sentiment_data]
    # # Categorize scores
    categories = ['Negative' if score < 0 else 'Positive' if score > 0 else 'Neutral' for score in sentiment_scores]
    # # Count scores in each category
    score_counts = Counter(categories)

    return jsonify({'sentiments': score_counts})


@app.route('/top_sources', methods=['GET'])
def get_top_sources():
    # Retrieve the text column and channel_name from the database
    articles_db = articles.query.filter(articles.source.isnot(None)).all()
        
    # Create a defaultdict of lists
    source_dict = defaultdict(list)
    
    sentiment_data = [(article.source, article.sentiment_score) for article in articles_db]

    # Group all same sources together
    for source, sentiment_score in sentiment_data:
        source_dict[source].append(sentiment_score)

    # Calculate the average sentiment score for each source
    average_scores = {source: {'average_score': sum(scores) / len(scores), 'count': len(scores)} for source, scores in source_dict.items()}
    # Sort the dictionary based on count in descending order and take the top 10
    top_10_sources = sorted(average_scores.items(), key=lambda x: x[1]['count'], reverse=True)[:10]
    top_sources_list = []
    for (source, avcnt) in top_10_sources:
        top_sources_list.append({
            "source": source,
            "count": avcnt['count'],
            "score": avcnt['average_score']
        })

    return jsonify({'top_channel_messages': top_sources_list})


@app.route('/date_article', methods=['GET'])
def get_date():
    # Retrieve the text column and channel_name from the database

    with app.app_context():
        # Group by publish date and count the number of articles
        result = db.session.query(cast(articles.date_published, Date), func.count(articles.title)).group_by(cast(articles.date_published, Date)).all()

    # Convert result to a dictionary
    # Convert result to a dictionary
    # Convert result to a dictionary
    data = {int(time.mktime(date.timetuple())): count for date, count in result}

    # Now you can send `data` as JSON
    print("the dataaa :", data)
    # iterate throught the data
    dt = []
    for key, value in data.items():
        # Convert the timestamp to an integer
        timestamp = int(key)

        # Convert the timestamp to a datetime object
        date = datetime.fromtimestamp(timestamp)

        # Extract the date in the format 'Jan 23'
        formatted_date = date.strftime('%b %d')
        dt.append({'date': formatted_date, 'articles': value})

    return jsonify({'data': dt})

if __name__ == '__main__':
    app.run()