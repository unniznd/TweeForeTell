from django.shortcuts import render

import joblib
import numpy as np

from .get_tweets import  get_recent_tweets
from .text_process import preprocess

def home(request):
    recent_tweets = get_recent_tweets()

    model = joblib.load('model.h5')
    print(model)

    valid_tweet_id = []
    for tweet in recent_tweets:
        if tweet.lang == 'en' and len(tweet.text) > 100:
            valid_tweet_id.append(
                {
                    'id':tweet.id,
                    'emotion':model.predict(np.array([tweet.text]))
                }
            )
            
    return render(
        request,
        'navbar/home.html',
        context={
            'recent_tweets':recent_tweets,
            'valid_tweet_id': valid_tweet_id
        }
    )
