#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    new_collection = []
    for doc in mongo_collection.find():
        count = 0
        total_score = 0
        for item in doc["topics"]:
            total_score += item["score"]
            count += 1
        if (count >= 1):
            doc["averageScore"] = total_score / count
        else:
            doc["averageScore"] = 0

        new_collection.append(doc)

    return sorted(new_collection, key=lambda x:
                  x["averageScore"], reverse=True)
