from database.mongodb import bookmarks_collection

from datetime import datetime



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



        "created_at": datetime.now()

    }


    result = bookmarks_collection.insert_one(
        document
    )


    return str(
        result.inserted_id
    )