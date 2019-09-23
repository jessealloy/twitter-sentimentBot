import twitter
from textblob import TextBlob as tb
from setUp import *
from getReplies import *
from twython import Twython
from twython import TwythonStreamer

def main():
    api,dictionary,twythonObject,stream = setUp()
    #twythonObject.search(q='python')
    #stream.statuses.filter(track='twitter')
    twythonObject.search(q='twitter', result_type='popular')

    print("Please select which user you are curious about by pasting the name into this input: ")
    for i in dictionary.keys():
        print(i)
    selection = "Donald Trump"#input("selection: ")
    replies = getReplies(api,dictionary.get(selection))
    for i in replies:
        print(i)

if __name__ == "__main__":
    main()
