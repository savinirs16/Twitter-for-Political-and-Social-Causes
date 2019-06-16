from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_secret = 'xxxx'


class listener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
            saveFile = open('naive.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException as e:
            print('failed ondata,',str(e))
            time.sleep(5)

def on_error(self, status):
    print(status)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=[ '#trumpyourthanksgiving'])




