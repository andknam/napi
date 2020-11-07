import requests
from sources import entertainment_sources, sports_sources, technology_sources

# based on query and radio button, filter my search
# this should return some list of tuple items
def search_engine(query, category):
    url_everything = 'http://newsapi.org/v2/everything?q='
    q = query

    # choosing the source type
    if category == 'entertainment':
        source = '&sources=' + entertainment_sources
    elif category == 'sports':
        source = '&sources=' + sports_sources
    else:
        source = '&sources=' + technology_sources

    apiKey = '&apiKey=78b9d599c4f94f8fa3afb1a5458928d6'

    # look at only the first page for now
    page = '&page=' + '1'

    search_url = url_everything + q + source + page + apiKey

    response = requests.get(search_url)
    json = response.json()

    # saving the results
    # format as a json so that i can use it in
    # {% for result in results %} ... {% endfor %} format
    results = []

    if json['status'] != 'ok':
        return 'bad status'

    if json['articles'] == []:
        return 'empty'

    for article in json['articles']:
        formatted_result = {}
        formatted_result['source'] = article['source']['name']
        formatted_result['title'] = article['title']
        formatted_result['description'] = article['description']
        formatted_result['url'] = article['url']
        formatted_result['urlToImage'] = article['urlToImage']
        formatted_result['publishedAt'] = article['publishedAt']
        results.append(formatted_result)

    return results
