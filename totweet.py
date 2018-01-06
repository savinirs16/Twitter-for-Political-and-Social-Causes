import tweepy
import csv

consumer_key = 'pkW6W1c3DCzT2ecuXAGqLjBVS'
consumer_secret = '6uD1r5nxZJASlPsGsvvGoHsQn4n38rcusIuiiwc4Mrbjy8NFSB'
access_token = '803328014121635840-CkGqI64IoYpOQeGBaVwXz0LnU1UbZdw'
access_secret = 'Uyo9Hw8CN0tEKPlWkMVGbCOk2pzcLh7f7ghm1BDBhhEo8'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

a = [];
i=0;
b='';
csvReader = csv.reader(open('usernames.csv', 'rb'));
for row in csvReader:
	a.append(row);
for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
    except:
        pass
for i in range(0, len(a)):
   message = "Show your thankfulness to Trump by paying through Paypal!! %s" %a[i]
   api.update_status(status=message)
   print('Message sent')