#!/usr/bin/env python3

from flask import Flask, jsonify, session
from flask_migrate import Migrate
from models import db, Article
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# REQUIRED for session handling
app.secret_key = "super-secret-key"

db.init_app(app)
migrate = Migrate(app, db)

# -------------------------
# PAYWALL ROUTE
# -------------------------
@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    session['page_views'] = session['page_views'] if 'page_views' in session else 0
    session['page_views'] += 1

    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    article = Article.query.get(id)

    if not article:
        return jsonify({'error': 'Article not found'}), 404

    return jsonify(article.to_dict()), 200

# -------------------------
# CLEAR SESSION ROUTE
# -------------------------
@app.route('/clear', methods=['GET'])
def clear():
    session.clear()
    return jsonify({'message': 'Session cleared'}), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
