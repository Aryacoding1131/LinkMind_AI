from collections import Counter


def recommend_bookmarks(current_bookmark, bookmarks):

    current_keywords = set(

        current_bookmark.get(
            "keywords",
            []
        )

    )

    recommendations = []

    for bookmark in bookmarks:

        if bookmark["_id"] == current_bookmark["_id"]:
            continue

        keywords = set(
            bookmark.get(
                "keywords",
                []
            )
        )

        score = len(
            current_keywords.intersection(
                keywords
            )
        )

        recommendations.append(

            {

                "bookmark": bookmark,

                "score": score

            }

        )

    recommendations.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return recommendations[:3]
