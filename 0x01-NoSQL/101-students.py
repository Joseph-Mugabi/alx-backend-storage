#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    n_collection = []
    for docu in mongo_collection.find():
        count = 0
        total_score = 0
        for item in docu["topics"]:
            total_score += item["score"]
            count += 1
        if (count >= 1):
            docu["averageScore"] = total_score / count
        else:
            docu["averageScore"] = 0

        n_collection.append(doc)

    return sorted(n_collection, key=lambda x:
                  x["averageScore"], reverse=True)
