import GetOldTweets3 as got
import pandas as pd

username = 'dexquoted'
count = 557
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username) \
    .setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
user_tweets = [[tweet.date, tweet.text] for tweet in tweets]
# Creation of dataframe from tweets list
tweets_df = pd.DataFrame(user_tweets)
tweets_df.to_csv('tweets.csv')
