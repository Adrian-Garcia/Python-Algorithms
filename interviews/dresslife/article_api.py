import requests
import json


def fix_dataset(data):
    for article in data:
        if article["num_comments"] is None:
            article["num_comments"] = 0

    return data


def get_data():
    data = []

    for p in range(5):
        page = p + 1
        apiRequest = requests.get(
            "https://jsonmock.hackerrank.com/api/articles?page=" + str(page)
        )
        articles = apiRequest.json()["data"]
        data.append(articles)

    return fix_dataset([item for sublist in data for item in sublist])


def sort_information(data):
    return list(reversed(sorted(data, key=lambda d: d["num_comments"])))


def get_top(data, limit):
    names = []
    for article in data:

        if article["title"] != None:
            names.append(article["title"])

        elif article["story_title"] != None:
            names.append(article["story_title"])

        if len(names) == limit:
            break

    return names


data = get_data()
data = sort_information(data)
print(get_top(data, 2))
