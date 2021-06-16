import tweepy
import os


# Function recieves event and context because GCP Scheduler requires it to
# recieve 2 parameters. These parameters are not used.
def tueaday_dog(event, context):
    # Credentials for loging in
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    # Test authentication
    if not api.verify_credentials():
        raise ValueError("Wrong credentials")
    print("API created")

    # Tweet Tueaday dog video
    api.update_status("Happy tueaday https://t.co/lg5eM2cUZD")
    print("Tweeted Tueaday dog video")
