import requests


def collector(N):
    result = []
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false")
    listOfDicts = response.json()
    for dict in listOfDicts[0:N]:
        result.append(dict['name'])
    return result
