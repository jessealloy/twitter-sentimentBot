import twitter
from textblob import TextBlob as tb
from setUp import *
from getReplies import *

def main():
    api,dictionary = setUp()
    print("Please select which user you are curious about by pasting the name into this input: ")
    for i in dictionary.keys():
        print(i)
    selection = input("selection: ")
    replies = getReplies(dictionary.get(selection))
    for i in replies:
        print(i)

if __name__ == "__main__":
    main()
