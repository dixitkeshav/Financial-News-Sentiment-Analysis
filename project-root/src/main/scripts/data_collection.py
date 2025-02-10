import requests
import json
from src.main.config import Config

def fetch_news():
    """Fetches latest financial news from an API."""
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={Config.NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        with open("../data/raw/news.json", "w") as f:
            json.dump(news_data, f, indent=4)
        print("News data saved successfully!")
    else:
        print("Error fetching news.")

if __name__ == "__main__":
    fetch_news()
