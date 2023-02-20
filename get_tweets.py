import tweepy
import pandas as pd

# twitter api auth
bearer_token = None
client = tweepy.Client(bearer_token)

query = '(elon musk) lang:en -is:retweet'


output = []
response = client.search_recent_tweets(query = query, max_results=100)
for tweet in response.data:
    text = tweet.text
    line = {'text' : text}
    output.append(line)

tweets_df = pd.DataFrame(output)
tweets_df.to_csv('elon_musk_tweets.csv')
