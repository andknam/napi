import requests
from sources import entertainment_sources, sports_sources, technology_sources, all_sources, language_iso

# based on query and radio button, filter my search
# this should return some list of tuple items
def advanced_search_engine(query, category, aTitle, sortBy, oldest, newest, add_sources, language):
    url_everything = 'http://newsapi.org/v2/everything?'

    # search for query in article title vs. search in article body
    if aTitle:
        q = 'qInTitle=' + query
    else:
        q = 'q=' + query

    # choosing the source type
    if add_sources == '':
        if category == 'entertainment':
            source = '&sources=' + entertainment_sources
        elif category == 'sports':
            source = '&sources=' + sports_sources
        else:
            source = '&sources=' + technology_sources

    # choosing specific sources
    else:
        source = '&sources='
        n = 0
        for num in add_sources:
            if n == 0:
                source += all_sources[int(num)]
                n += 1
            else:
                source += ',' + all_sources[int(num)]

    search_url = url_everything + q + source

    # sortBy
    search_url += '&sortBy=' + sortBy[1:]

    # published date
    if oldest:
        search_url += '&from=' + oldest
    if newest:
        search_url += '&to=' + newest

    # language
    if language:
        search_url += '&language=' + language_iso[int(language)]

    # check if its a valid search / check num of results
    search_url_check = search_url + '&page=' + '1' + '&apiKey=78b9d599c4f94f8fa3afb1a5458928d6'

    response = requests.get(search_url_check)
    json = response.json()

    # error messages
    if json['status'] != 'ok' or json['status'] == 'error':
        return 'bad status'
    if json['articles'] == []:
        return 'empty'

    # saving the results
    # format as a json so that i can use it in
    # {% for result in results %} ... {% endfor %} format
    results = []

    num_results = json['totalResults']
    num_pages = num_results // 20
    num_pages = min(num_pages, 6)

    for i in range(1, num_pages):
        # look at only the first five pages (huge search results dont render well)
        search_url_paged = search_url + '&page=' + str(i) + '&apiKey=78b9d599c4f94f8fa3afb1a5458928d6'
        response = requests.get(search_url_paged)
        json = response.json()

        for article in json['articles']:
            formatted_result = {}
            formatted_result['source'] = article['source']['name']
            formatted_result['title'] = article['title']
            formatted_result['description'] = article['description']
            formatted_result['url'] = article['url']
            formatted_result['urlToImage'] = article['urlToImage']
            formatted_result['publishedAt'] = article['publishedAt']
            results.append(formatted_result)

    # reversedPublishedAt
    if sortBy[0] == '1':
        results = results[::-1]

    # check for empty results
    if results == []:
        return 'empty'

    return results
