import twitter

def getReplies(api,user):
    api.GetUser(user)
    replies = api.getReplies()
    return replies
