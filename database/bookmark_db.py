from datetime import datetime

from database.mongodb import get_bookmark_collection

from bson import ObjectId

collection = get_bookmark_collection()



def save_bookmark(
        user_id,
        bookmark
):


    document = {


        "user_id": user_id,


        "url": bookmark["url"],

        "domain": bookmark["domain"],

        "title": bookmark["title"],

        "description": bookmark["description"],

        "content": bookmark["content"],


        "headings": bookmark["headings"],


        "word_count": bookmark["word_count"],



        # NLP

        "keywords": bookmark["keywords"],

        "entities": bookmark["entities"],

        "reading_time": bookmark["reading_time"],



        # Ollama

        "category": bookmark["category"],

        "confidence": bookmark["confidence"],

        "ai_tags": bookmark["ai_tags"],



        # Groq

        "summary": bookmark["summary"],

        "key_points": bookmark["key_points"],

        "difficulty": bookmark["difficulty"],

        "audience": bookmark["audience"],



        "created_at": datetime.utcnow()

    }



    result = collection.insert_one(
        document
    )


    return result.inserted_id


def get_user_bookmarks(user_id):

    collection = get_bookmark_collection()

    bookmarks = collection.find(
        {
            "user_id": user_id
        }
    ).sort(
        "created_at",
        -1
    )

    return list(bookmarks)



def delete_bookmark(bookmark_id):

    collection = get_bookmark_collection()

    result = collection.delete_one(
        {
            "_id": ObjectId(bookmark_id)
        }
    )

    return result.deleted_count > 0

from database.mongodb import get_bookmark_collection


def search_bookmarks(user_id, search_text):

    collection = get_bookmark_collection()

    bookmarks = collection.find({

        "user_id": user_id,

        "$or": [

            {"title": {"$regex": search_text, "$options": "i"}},

            {"url": {"$regex": search_text, "$options": "i"}},

            {"category": {"$regex": search_text, "$options": "i"}},

            {"keywords": {"$regex": search_text, "$options": "i"}}

        ]

    })

    return list(bookmarks)
