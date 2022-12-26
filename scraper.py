# source: https://www.youtube.com/watch?v=jtIMnmbnOFo&ab_channel=AISpectrum

import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys
  
# Print search terms entered in terminal
print("\nSearch terms entered:", sys.argv[1])

query = f"{sys.argv[1]} since:2022-12-24"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('tweets.csv')