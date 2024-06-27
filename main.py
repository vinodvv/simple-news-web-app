from flask import Flask, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = 'a302356f277a41889d72ea20e3f97d60'
NEW_API_URL = 'https://newsapi.org/v2/top-headlines?country=in&language=en&apiKey=' + NEWS_API_KEY


@app.route('/')
def home():
    """
    Fetches the top headlines from NewsAPI and renders them on the home.html template.
    :return:
    str: The rendered HTML content for the home page, displaying the list of news articles.
    """
    response = requests.get(NEW_API_URL)
    news_data = response.json()
    articles = news_data.get('articles', [])
    return render_template('home.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
