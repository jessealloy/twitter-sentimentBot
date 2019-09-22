import twitter
from textblob import TextBlob as tb

api = twitter.Api(consumer_key="d28kNSvpJzRGSnyMIVyGJyDBG",
                  consumer_secret="Y5Fq7VaeQLJ8FIBpxmly979fygklL4etUQZD14O9mUUebJIXjg",
                  access_token_key="2194488412-keCEXYHHWTYkSkzWmnEMkP8bEo6GxDNPOFAQEEv",
                  access_token_secret="Fu33eGGRZvDllkV1nelQi0LEYuW1kks7zc4VouJ0xvuck")

statuses = api.GetUserTimeline(25073877)
for i in statuses:
    print(tb(i.text).sentiment)
