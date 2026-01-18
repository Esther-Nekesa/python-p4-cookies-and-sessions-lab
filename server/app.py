from flask import Flask, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)

# Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author
        }

# Route to get an article
@app.route('/articles/<int:id>')
def get_article(id):
    # Initialize page_views if first time
    session['page_views'] = session.get('page_views', 0) + 1

    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    article = db.session.get(Article, id)
    if not article:
        return jsonify({'message': 'Article not found'}), 404

    return jsonify(article.to_dict())

# Route to clear session
@app.route('/clear')
def clear_session():
    session.clear()
    return jsonify({'message': 'Session cleared'})

if __name__ == '__main__':
    app.run(debug=True)
