import os
import random
import time
import dotenv
import tweepy

dotenv.load_dotenv(dotenv.find_dotenv())

key = os.getenv("key")
secret = os.getenv("secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

pessoas = 0


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global pessoas
        try:
            user_do_mlk = str(status.text).split(" ")[0]

            def gerar_reply():
                nonlocal user_do_mlk
                user_do_mlk = str(status.text).split(" ")[0]
                if user_do_mlk[0] == '@' and user_do_mlk != '@MusicaFoxBot':
                    reply = f"slk, {user_do_mlk} é abusado em campo https://twitter.com/i/status/1379858855933452288" \
                            f"/video/1 "
                else:
                    reply = "slk, mlk é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"

            if user_do_mlk != 'RT':
                reply_1 = "slk, mlk é abusado em campo https://twitter.com/i/status/1379858855933452288/video/1"
                reply_2 = "slk, mlk é abusado em campo https://twitter.com/i/status/1388566886372237312/video/1"
                replys = [reply_1, reply_2]
                reply = random.choice(replys)
                api.update_status(status=reply, in_reply_to_status_id=status.id,
                                  auto_populate_reply_metadata=True)

                pessoas += 1
                print(f"Answering to @{status.user.screen_name}")

            else:
                print(f"Skipping RT")

            time.sleep(36.69)
        except tweepy.TweepError as e:
            print(e.reason, '--')
        except StopIteration:
            print('Error')


if __name__ == "__main__":
    print("Bot started")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['#musicafoxbot', '#mscfoxbot'])
