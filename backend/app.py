from collections import Counter, defaultdict
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

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
    sentiment_score = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Channel_messages_ts: id={self.id}, channel_name={self.source}, text={self.sentiment_score}, timestamp_events={self.timestamp}"

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
    article_data = articles.query.all()
    print("The article dataaaa: ", article_data)
    article_list = []

    for article in article_data:
        article_list.append({
            "category": f"Category {article.category}",
            "title": article.title,  # Correct column name
            "content": article.content  # Correct column name
        })

    return jsonify({'articles': article_list})


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

    print("The Average Scoreeeee: ",top_10_sources)

    # Extract text and channel_name from each message
    # articles_data = [(article.source) for article in articles_db]

    # # # Calculate the frequency of each unique article
    # _freq = Counter(articles_data)

    # top_sources = _freq.most_common(10)

    # print("The Top of Tops: ", top_10_sources)
    top_sources_list = []
    for (source, avcnt) in top_10_sources:
        top_sources_list.append({
            "source": source,
            "count": avcnt['count'],
            "score": avcnt['average_score']
        })

    return jsonify({'top_channel_messages': top_sources_list})

if __name__ == '__main__':
    app.run()