# NAPI

Link to live site: http://napi.pythonanywhere.com/

### What it does:
NAPI is a search web application that allows users to enter in search word(s) along with a specific category to 
find results from the web. The basic search only requires the user to enter in any search query and 
choose a category. Users can choose the advanced search option to specify their search query,
search for words in the article title, sort by factors such as relevancy and popularity,
alter the publish range, choose specific news sources, and even the language of the news sorce.

The results page for both the basic and advanced search display the article image, article title,
news source, publish time, and the article description.

### How I built it:
The application was built with Flask (a Python web framework), Materialize (a front-end framework based on Material Design),
and the News API.

### Challenges that I ran into:
Materialize is a really simple and awesome framework for people looking to work with front-end, but since it was my first time
I had some trouble implementing an autocomplete input field with chips for the news sources (I opted for an options dropdown instead). 
I also had some trouble connecting the select values from the select boxes to work with the Flask request 
form since not all values in the advanced search form had to be used. The other big hurdle was deciding how to use the output of the sources
endpoint to search for articles using the everything endpoint. 

There are also a few things I'd like to improve or extend about my application if I had more time:
* Implement the bonus - I was able to figure out that sites such as the WSJ had some sort of 
paywallType attribute within the source code, but wasn't quite able to figure out how to implement
paywall detection outside of manually going through each news source. 
* Link history - It would be a good idea for users to be able to save links they have visited or wish to visit in the future.
* Voice search - I have some experience working with the Alexa Skill SDK, so it would be really cool to extend 
the web application to work with voice as well. 

### Accomplishments I'm proud of:
Although this was my first time working with Materialize, I was able to use the framework to create a clean-looking application
(which is really important considering that search results should be easy to read). I also have never worked with the News API before,
so this gave me an opportunity to read through API documentation and figure out how things fit together. Overall, I'm happy how the search engine turned out. 


