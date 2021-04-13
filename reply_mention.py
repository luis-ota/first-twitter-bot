import tweepy
import time
import logging
import dotenv
import os
from datetime import datetime


now = datetime.now()
dotenv.load_dotenv(dotenv.find_dotenv())

key = os.getenv("key")
secret = os.getenv("secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        logger.info("Retrieving mentions")
        try:
            api.update_status(
                status=reply, in_reply_to_status_id=status.id,
                auto_populate_reply_metadata=True
            )
            
            logger.info(f"Answering to {status.user.name}")
            logger.info("Message sended")
            
            time.sleep(169)
        except tweepy.TweepError as e:
            print(e.reason, '--')
        except StopIteration:
            print('deu ruim')
    
if __name__ == "__main__":
    logger.info(f"Bot started at {now}")
    myStreamListener = MyStreamListener()
    reply = "slk, mlk é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['#musicafoxbot', '#mscfoxbot'])
