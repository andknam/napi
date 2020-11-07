import requests

# filters the sources into entertainment, sports, and technology
url = ('http://newsapi.org/v2/sources?'
       'apiKey=78b9d599c4f94f8fa3afb1a5458928d6')

response = requests.get(url)
json = response.json()

# split all named sources into 3 categories
entertainment_sources = []
sports_sources = []
technology_sources = []

# splitting of sources into categories
for source in json['sources']:
    source_url = source['id']

    # entertainment, sports, and technology
    if source['category'] == 'entertainment':
        entertainment_sources.append(source_url)
    elif source['category'] == 'sports':
        sports_sources.append(source_url)
    elif source['category'] == 'technology':
        technology_sources.append(source_url)

    # thought about doing this, but search results were never specific enough
    # elif source['category'] == 'general':
    #    entertainment_sources.append(source_url)
    #    sports_sources.append(source_url)
    #    technology_sources.append(source_url)

entertainment_sources = ','.join(entertainment_sources)
sports_sources = ','.join(sports_sources)
technology_sources = ','.join(technology_sources)

all_sources = {0: 'abc-news', 1: 'abc-news-au', 2: 'aftenposten', 3: 'al-jazeera-english',
4: 'ansa', 5: 'argaam', 6: 'ars-technica', 7: 'ary-news', 8: 'associated-press',
9: 'australian-financial-review', 10: 'axios', 11: 'bbc-news', 12: 'bbc-sport', 13: 'bild',
14: 'blasting-news-br', 15: 'bleacher-report', 16: 'bloomberg', 17: 'breitbart-news',
18: 'business-insider', 19: 'business-insider-uk', 20: 'buzzfeed', 21: 'cbc-news',
22: 'cbs-news', 23: 'cnn', 24: 'cnn-es', 25: 'crypto-coins-news', 26: 'der-tagesspiegel',
27: 'die-zeit', 28: 'el-mundo', 29: 'engadget', 30: 'entertainment-weekly', 31: 'espn',
32: 'espn-cric-info', 33: 'financial-post', 34: 'focus', 35: 'football-italia', 36: 'fortune',
37: 'four-four-two', 38: 'fox-news', 39: 'fox-sports', 40: 'globo', 41: 'google-news',
42: 'goteborgs-posten', 43: 'gruenderszene', 44: 'hacker-news', 45: 'handelsblatt', 46: 'ign',
47: 'il-sole-24-ore', 48: 'independent', 49: 'infobae', 50: 'info-money', 51: 'la-gaceta',
52: 'la-nacion', 53: 'la-repubblica', 54: 'le-monde', 55: 'lenta', 56: 'lequipe', 57: 'les-echos',
58: 'liberation', 59: 'marca', 60: 'mashable', 61: 'medical-news-today', 62: 'msnbc', 63: 'mtv-news',
64: 'mtv-news-uk', 65: 'national-geographic', 66: 'national-review', 67: 'nbc-news', 68: 'news24',
69: 'new-scientist', 70: 'news-com-au', 71: 'newsweek', 72: 'new-york-magazine', 73: 'next-big-future',
74: 'nfl-news', 75: 'nhl-news', 76: 'nrk', 77: 'politico', 78: 'polygon', 79: 'rbc',
80: 'recode', 81: 'reddit-r-all', 82: 'reuters', 83: 'rt', 84: 'rte', 85: 'rtl-nieuws',
86: 'sabq', 87: 'spiegel-online', 88: 'svenska-dagbladet', 89: 't3n', 90: 'talksport',
91: 'techcrunch', 92: 'techcrunch-cn', 93: 'techradar', 94: 'the-american-conservative',
95: 'the-globe-and-mail', 96: 'the-hill', 97: 'the-hindu', 98: 'the-huffington-post',
99: 'the-irish-times', 100: 'the-jerusalem-post', 101: 'the-lad-bible', 102: 'the-next-web',
103: 'the-sport-bible', 104: 'the-times-of-india', 105: 'the-verge', 106: 'the-wall-street-journal',
107: 'the-washington-post', 108: 'the-washington-times', 109: 'time', 110: 'usa-today',
111: 'vice-news', 112: 'wired', 113: 'wired-de', 114: 'wirtschafts-woche', 115: 'xinhua-net',
116: 'ynet'}

language_iso = {1: 'ar', 2: 'de', 3: 'en', 4: 'es', 5: 'fr', 6: 'he', 7: 'it', 8: 'nl',
9: 'no', 10: 'pt', 11: 'ru', 12: 'se', 13: 'zh'}
