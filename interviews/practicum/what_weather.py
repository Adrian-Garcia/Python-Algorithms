import requests

cities = [
    "Rio de Janeiro",
    "Istanbul",
    "Jakarta",
    "Tbilisi",
    "Beijinq",
    "Paris",
    "Mexico City",
]


def make_url(city):
    # Specify the required city in the URL
    return f"http://wttr.in/{city}"


def make_parameters():
    params = {
        "format": 2,  # Set single-line output
        "M": "",  # Wind speed in meters per second
    }
    return params


def what_weather(city):
    url = make_url(city)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text

        return "<server error>"

    except requests.ConnectionError:
        raise "<network error>"


print("Weather in:")
for city in cities:
    print(city, what_weather(city))
