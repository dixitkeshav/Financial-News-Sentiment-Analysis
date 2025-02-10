import os

class Config:
    # Get absolute project root path dynamically
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Paths (Ensure they are absolute)
    RAW_DATA_PATH = os.path.join(BASE_DIR, "..", "data", "raw")
    PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "..", "data", "processed")
    MODEL_PATH = os.path.join(BASE_DIR, "..", "models")

    # API Configuration
    NEWS_API_KEY = os.getenv("NEWS_API_KEY", "your_news_api_key_here")  # Uses environment variable if available
    
    # NLP Settings
    STOPWORDS_LANGUAGE = "english"
    
    # Model Parameters
    MODEL_NAME = "bert-base-uncased"

# Example usage
if __name__ == "__main__":
    print("Raw Data Path:", Config.RAW_DATA_PATH)
    print("Processed Data Path:", Config.PROCESSED_DATA_PATH)
    print("Model Path:", Config.MODEL_PATH)
    print("News API Key:", Config.NEWS_API_KEY)
