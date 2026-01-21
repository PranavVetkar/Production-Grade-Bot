import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class TradingBrain:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.prices = []

    def get_sentiment(self, text):
        score = self.sia.polarity_scores(text)['compound']
        return score

    def calculate_indicators(self, price_list):
        if len(price_list) < 20: return "WAIT"
        df = pd.DataFrame(price_list, columns=['close'])
        sma_20 = df['close'].rolling(window=20).mean().iloc[-1]
        
        current_price = price_list[-1]
        return "BULLISH" if current_price > sma_20 else "BEARISH"