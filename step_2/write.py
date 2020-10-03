import os, tweepy

from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))

api = tweepy.API(auth)

api.update_status("Confirming that we're able to post a message to Twitter with Python from a Raspberry Pi")
