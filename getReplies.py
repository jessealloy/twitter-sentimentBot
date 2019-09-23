import twitter
import json

def getReplies(api,user):
    userObj = api.GetUser(user)
    replies = api.GetReplies(user)
    print(replies)
    return replies
