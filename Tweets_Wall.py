# Tweepy Library
import tweepy

# Pandas Library
import pandas as pd

# Consumer key
ckey="7Od6SlMHXUDA09Jjas5oQ5N4v"
# Consumer Secret Key
csecret="tLDplZEwLAktgnRy1406wvO5PRqLHMUsiPnwiwZrebMDMx4CA4"
# Access Token
atoken="933370862681624576-eOuTV5RlPbTh3suQEYDzI2iqhGFiMXX"
# Access Secret
asecret="VGYtjzESseJUuVauTd0oOMv7tpXKlTWAzJmJSVNKZEU8N"

# Handler with consumer key and consumer secret key
auth = tweepy.OAuthHandler(ckey, csecret)

# Access with access token and Access Secret
auth.set_access_token(atoken, asecret)

# API
api = tweepy.API(auth)

# DataFrame with two columns
df = pd.DataFrame(columns=['Text','DateTime'])

# Tweets collection with loop
for status in tweepy.Cursor(api.user_timeline, screen_name='@AsadMaharvi', tweet_mode="extended").items():
        # Print the tweet Text
        print(status.full_text)

        # Append DataFrame with tweet text and datetime
        df = df.append({'Text': str(status.full_text), 'DateTime': str(status.created_at)}, ignore_index=True)

# Finally save dataframe as csv file
df.to_csv('Data.csv')