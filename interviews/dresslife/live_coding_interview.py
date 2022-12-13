import requests
import json
import pprint

API_LINK = "https://jsonplaceholder.typicode.com/posts/"


def get_posts() -> list:
    posts = []
    for page in range(10):
        pageLink = API_LINK + str(page + 1)
        apiPostRequest = requests.get(pageLink)
        apiCommentsRequest = requests.get(pageLink + "/comments")
        post = apiPostRequest.json()
        post["comments"] = apiCommentsRequest.json()
        posts.append(post)

    return posts


def get_domains(posts: list) -> dict:
    domains = dict()
    for post in posts:
        for comment in post["comments"]:
            at_index = comment["email"].index("@") + 1
            current_domain = comment["email"][at_index:].split(".", 1)[1]

            if current_domain in domains:
                domains[current_domain] += 1
                continue

            domains[current_domain] = 1

    return domains


def solution() -> dict:
    posts = get_posts()
    domains = get_domains(posts)
    return domains


# pprint.pprint(get_posts())
# pprint.pprint(solution())
