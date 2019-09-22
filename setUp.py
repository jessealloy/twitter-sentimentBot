import twitter

def setUp():
    api = twitter.Api(consumer_key="d28kNSvpJzRGSnyMIVyGJyDBG",
                      consumer_secret="Y5Fq7VaeQLJ8FIBpxmly979fygklL4etUQZD14O9mUUebJIXjg",
                      access_token_key="2194488412-keCEXYHHWTYkSkzWmnEMkP8bEo6GxDNPOFAQEEv",
                      access_token_secret="Fu33eGGRZvDllkV1nelQi0LEYuW1kks7zc4VouJ0xvuck")

    dictionary = buildUserIDMap("usersdataraw.txt")
    return api,dictionary

def buildUserIDMap(fileName):
    file = open(fileName)
    dictionary = {}
    for line in file:
        line = line.split(",")
        dictionary[line[0]] = line[1]
    return dictionary
