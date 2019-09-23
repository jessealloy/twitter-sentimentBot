import twitter
from twython import Twython
from twython import TwythonStreamer as MyStreamer
import sys

def setUp():

    APP_KEY = 'd28kNSvpJzRGSnyMIVyGJyDBG'
    APP_SECRET = 'Y5Fq7VaeQLJ8FIBpxmly979fygklL4etUQZD14O9mUUebJIXjg'
    OAUTH_TOKEN = '2194488412-keCEXYHHWTYkSkzWmnEMkP8bEo6GxDNPOFAQEEv'
    OAUTH_TOKEN_SECRET = 'Fu33eGGRZvDllkV1nelQi0LEYuW1kks7zc4VouJ0xvuck'

    twythonObject = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    dictionary = buildUserIDMap("usersdataraw.txt")
    api = twitter.Api(consumer_key="d28kNSvpJzRGSnyMIVyGJyDBG",
                      consumer_secret="Y5Fq7VaeQLJ8FIBpxmly979fygklL4etUQZD14O9mUUebJIXjg",
                      access_token_key="2194488412-keCEXYHHWTYkSkzWmnEMkP8bEo6GxDNPOFAQEEv",
                      access_token_secret="Fu33eGGRZvDllkV1nelQi0LEYuW1kks7zc4VouJ0xvuck")
    user = dictionary['Donald Trump']
    user_tweets = twythonObject.get_user_timeline(screen_name='realDonaldTrump',
                                        include_rts=True)
    results = twythonObject.cursor(twythonObject.search, q='@realDonaldTrump', since_id=user_tweets[0]['id'])

    for result in results:
        if (result['text'].split(" ")[0] != 'RT') and (result['in_reply_to_screen_name'] == 'realDonaldTrump'):
            print(result['text'])
    sys.exit(1)

    return api,dictionary,twythonObject

def buildUserIDMap(fileName):
    file = open(fileName)
    dictionary = {}
    for line in file:
        line = line.split(",")
        dictionary[line[0]] = line[1]
    return dictionary
