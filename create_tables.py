from shop import create_app, db
#from shop.models import User  # Ensure models are imported so SQLAlchemy knows about them

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created")
