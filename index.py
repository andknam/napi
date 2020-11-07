from flask import Flask, render_template, request
from search_engine import search_engine
from advanced_search_engine import advanced_search_engine

app = Flask(__name__)
app.config['DEBUG'] = True

# basic search
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['term']
        category = request.form['category']
        results = search_engine(query, category)

        results = check_results(results)

        return render_template('search.html', results = results)

    return render_template('index.html')

# advanced search
@app.route("/advanced_index", methods=['GET', 'POST'])
def advanced_index():
    if request.method == 'POST':
        query = request.form['term']
        category = request.form['category']

        # sortBy
        if request.form['sortBy'] == '1':
            sortBy = '1publishedAt'
        elif request.form['sortBy'] == '2':
            sortBy = '0relevancy'
        elif request.form['sortBy'] == '3':
            sortBy = '0popularity'
        else:
            sortBy = '0publishedAt'

        # publish range
        if request.form['oldest']:
            oldest = request.form['oldest']
        else:
            oldest = ''
        if request.form['newest']:
            newest = request.form['newest']
        else:
            newest = ''

        # query in article title as opposed to article body
        aTitle = request.form.get('articleTitle')
        if aTitle:
            aTitle = request.form['articleTitle']
        else:
            aTitle = ''

        # choose specific sources
        add_sources = request.form.getlist('add_sources')
        if add_sources:
            add_sources = request.form.getlist('add_sources')
        else:
            add_sources = ''

        # language
        if request.form['language'] != '0':
            language = request.form['language']
        else:
            language = ''

        results = advanced_search_engine(query, category, aTitle, sortBy, oldest, newest, add_sources, language)

        search_results = check_results(results)

        return render_template('advanced_search.html', search_results=search_results)

    return render_template('advanced_index.html')

def check_results(results):
    if results == 'bad status':
        results = [{'description': 'Oh no there was something wrong with the API status! Try changing your search.'}]

    if results == 'empty':
        results = [{'description': 'Oh no there were no articles! Try changing your search.'}]

    return results
