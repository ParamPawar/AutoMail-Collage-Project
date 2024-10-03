# db.py
from pymongo import MongoClient

# Set up MongoDB connection
def get_db():
    client = MongoClient('mongodb://localhost:27017/')  # Use your MongoDB URI
    db = client['AutoMail-Collage-Project']  # Replace with your database name
    return db['users']  # Replace with your collection name
# my url mongodb://localhost:27017