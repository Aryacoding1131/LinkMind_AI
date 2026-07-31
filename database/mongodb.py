from pymongo import MongoClient
from config.settings import MONGO_URI, DATABASE_NAME


# MongoDB Connection

client = MongoClient(
    MONGO_URI
)


db = client[
    DATABASE_NAME
]


# Collections

bookmarks_collection = db["bookmarks"]

users_collection = db["users"]



def get_bookmark_collection():

    return bookmarks_collection



def get_user_collection():

    return users_collection