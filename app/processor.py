from app.fetcher import Dal
import pandas as pd
# import dependencies
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Analysis:

    def __init__(self):
        self.data = Dal().get_all()
        self.df = pd.DataFrame(self.data)
        self.df_text = self.df["Text"]
        self.my_dict = {}


    def the_rarest_word(self):
        # count = 0
        # for words in self.df_text.str.split():
        #     for word in words:
        #         print(word)
        #     print(1)
        pass

    def finding_the_feel_of_the_text(self):
    #     score=SentimentIntensityAnalyzer().polarity_scores()
        pass

if __name__ == "__main__":
    a = Analysis()
    a.the_rarest_word()


