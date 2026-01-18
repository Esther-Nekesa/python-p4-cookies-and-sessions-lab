from app import db, Article, app

with app.app_context():
    # Drop all tables (for fresh start)
    db.drop_all()
    db.create_all()

    # Seed articles
    articles = [
        Article(title="First Post", content="This is the first article.", author="Alice"),
        Article(title="Second Post", content="This is the second article.", author="Bob"),
        Article(title="Third Post", content="This is the third article.", author="Charlie"),
        Article(title="Fourth Post", content="This is the fourth article.", author="Diana"),
    ]

    for article in articles:
        db.session.add(article)
    db.session.commit()

    print("Seeded articles successfully!")
