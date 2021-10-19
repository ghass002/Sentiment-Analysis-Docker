#import modules
from germansentiment import SentimentModel
import sys 

def run(texts):
    """
    Run the germansentiment model
    Inputs:
    ------------------------------
    texts: list of strings
    """
    model = SentimentModel()      
    result = model.predict_sentiment(texts)
    print(result)

if _name_ == "_main_":
    run(sys.argv[1:])