import requests

# The API endpoint
def get_quote_of_the_day(category):
    payload = {}
    headers = {
    'Authorization': 'Bearer 5VBpAQizmbAX1HaN1exhBbm8AbtzKrcRx8sGKx8s',
}
    url = "https://quotes.rest/qod?language=en&category={}".format(category)

    # A GET request to the API
    res = requests.request("GET", url, headers=headers, data=payload)
    data = res.json()
    status = res.status_code
    match status:
        case 200:
            quote = data['contents']['quotes'][0]['quote']
        case 400:
            quote = data['error']['message']
        case _:
            quote = "Sorry, could not get the data"
    return quote

quote = get_quote_of_the_day(category="inspire")
print(quote)

