import tweepy
import time
import logging
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
reply=None

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global reply
        try:  
            user_do_mlk = str(status.text).split(" ")[0]          
            def gerar_reply(): 
                user_do_mlk = str(status.text).split(" ")[0]
                if user_do_mlk[0] == '@' and user_do_mlk != '@MusicaFoxBot':
                    reply = f"slk, {user_do_mlk} é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"
                else:
                    reply = "slk, mlk é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"
            
            if user_do_mlk != 'RT':
                reply = "slk, mlk é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"
                api.update_status(status=reply, in_reply_to_status_id=status.id,
                                  auto_populate_reply_metadata=True)
                                
                logger.info(f"Answering to {status.user.name}")
                logger.info("Message sended")
                logger.info("Retrieving mentions")              
            else:
                logger.info(f"Skiping RT")
            time.sleep(169)
        except tweepy.TweepError as e:
            print(e.reason, '--')
        except StopIteration:
            print('Erro')
        
    
if __name__ == "__main__":
    logger.info("Bot started")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['#musicafoxbot', '#mscfoxbot'])
