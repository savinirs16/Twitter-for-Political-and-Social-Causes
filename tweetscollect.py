from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key = 'pkW6W1c3DCzT2ecuXAGqLjBVS'
consumer_secret = '6uD1r5nxZJASlPsGsvvGoHsQn4n38rcusIuiiwc4Mrbjy8NFSB'
access_token = '803328014121635840-CkGqI64IoYpOQeGBaVwXz0LnU1UbZdw'
access_secret = 'Uyo9Hw8CN0tEKPlWkMVGbCOk2pzcLh7f7ghm1BDBhhEo8'


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




