from app import app
from models import db, Article

with app.app_context():
    Article.query.delete()

    article1 = Article(
        title='First Post',
        content='This is the first article.',
        author='Alice',
        preview='This is the first...'
    )

    article2 = Article(
        title='Second Post',
        content='This is the second article.',
        author='Bob',
        preview='This is the second...'
    )

    article3 = Article(
        title='Third Post',
        content='This is the third article.',
        author='Carol',
        preview='This is the third...'
    )

    db.session.add_all([article1, article2, article3])
    db.session.commit()
