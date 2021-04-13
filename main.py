import tweepy
import logging
import time
import dotenv
import os



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


def check_mentions(api, since_id, reply):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        try:
            new_since_id = max(tweet.id, new_since_id)
            
            if tweet.in_reply_to_status_id is not None:
                continue

            logger.info(f"Answering to {tweet.user.name}")

            api.update_status(
                status=reply,
                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True, include_entities=True
            )
            print('foi')
            
            
            exit()
        except tweepy.TweepError as e:
            print(e.reason, '--')
        except StopIteration:
            break

def main():
    since_id = 1
    reply = "slk, mlk é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"
    while True:
        since_id = check_mentions(api, since_id, reply)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
