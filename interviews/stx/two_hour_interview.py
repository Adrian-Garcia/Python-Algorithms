import requests
from datetime import datetime

KEY = "28dd1990"


def get_sales():
    try:
        response = requests.get(url=f"https://my.api.mockaroo.com/sales.json?key={KEY}")

        if response.status_code == 200:
            return response.json()

        return []

    except ConnectionError as e:
        print(e)
        return []


def format_summaries(categories):
    summaries = []

    for category in categories:
        summaries.append({"category": category, "total": categories[category]})

    return summaries


def get_summaries(sales):
    categories = dict()

    print(sales[1])

    for sale in sales:

        if sale["status"] != "CONFIRMED":
            continue

        for item in sale["items"]:
            category = item["category"]
            current_price = item["unit_price"] * item["amount"]

            if category in categories:
                categories[category] += current_price

            else:
                categories[category] = current_price

    return format_summaries(categories)


# {
#     "status": "CONFIRMED",
#     "created_date": "2021-10-07T05:46:11Z",
#     "sent_date": "2022-03-22T12:47:23Z",
#     "items": [
#         {"name": "Milk", "category": "Dairy", "amount": 2, "unit_price": 2.5},
#         {
#             "name": "Yellow cheese",
#             "category": "Dairy",
#             "amount": 0.2,
#             "unit_price": 29.99,
#         },
#         {"name": "Beer", "category": "Drinks", "amount": 4, "unit_price": 3.99},
#     ],
# },
def render_summaries(summaries):
    for summary in summaries:
        print(f"{summary['category']} - {summary['total']:.2f}")


def get_average_processing_time(sales):
    sales_sum = 0
    count = 0

    for sale in sales:
        sent_date = sale["sent_date"]
        created_date = sale["created_date"]

        if sent_date and created_date:
            datetime_sent_date = datetime.fromisoformat(sent_date)
            datetime_created_date = datetime.fromisoformat(created_date)

            difference = datetime_sent_date - datetime_created_date
            seconds_in_day = 24 * 60 * 60
            min_and_sec = divmod(
                difference.days * seconds_in_day + difference.seconds, 60
            )

            time_elapsed = min_and_sec[0] * min_and_sec[1]

            sales_sum += time_elapsed
            count += 1

    return sales_sum / count


def main():
    sales = get_sales()
    print(sales[1])
    # summaries = get_summaries(sales)
    # render_summaries(summaries)

    average = get_average_processing_time(sales)
    print(average)


if __name__ == "__main__":
    main()
