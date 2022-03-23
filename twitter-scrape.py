import tweepy
import pandas

def CalcRemainingPulls(pullDataPath,sourceName):
    with open(pullDataPath,'r') as pullDataFile:


def TweetScrape(hashtags, from_date, countTweets):


def CollectTweets(keyPath="Twitter Keys"):
    # Enter your own credentials obtained
    # from your developer account
    with open(keyPath,'r') as keyFile:
        isLabel = True
        keyArray = []
        for line in keyFile:
            if isLabel:
                print("Retrieving " + line)
            else:
                keyArray.append(line.rstrip("\n"))
            isLabel = not(isLabel)
    if debug:
        print(keyArray)
    [consumer_key,consumer_secret,bearer_key,access_key,access_secret] = keyArray

    if debug:
        print(consumer_key)
        print(access_secret)

    # Set Twitter Access
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Enter Hashtag and initial date
    print("Enter Twitter HashTag to search for")
    words = input()
    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    date_since = input()

    # number of tweets you want to extract in one run
    numtweet = 100
    TweetScrape(words, date_since, numtweet)
    print('Scraping has completed!')

if __name__ == '__main__':
    debug = True
    CollectTweets()
