import tweepy
import pandas as pd

class TwitterHandler:
    def __init__(self):
        self.tweetData = pd.DataFrame(columns=['username',
                                            'description',
                                            'location',
                                            'following',
                                            'followers',
                                            'totaltweets',
                                            'retweetcount',
                                            'text',
                                            'hashtags'])

    def CalcRemainingPulls(pullDataPath,sourceName):
        with open(pullDataPath,'r') as pullDataFile:
            pass

    def TweetScrape(words, from_date, countTweets):
        # Clear Data Frame for the tweet data

        self.tweetData = pd.DataFrame(columns=self.tweetData.columns)

        # Search Twitter using a cursor
        tweetsIterator = tweepy.Cursor(api.search_tweets, words,
                                lang="en", since_id=from_date,
                                tweet_mode='extended').items(countTweets)

        # Put data into list from iterator and check to ensure list is populated
        tweetsList = [tweet for tweet in tweetsIterator]
        if len(tweetsList) == 0:
            print("No tweets scraped, exiting function...")
            return

        # Init tweet counter
        i = 0

        # Break tweet data into attributes and append to Data DataFrame
        for tweet in tweetsList:

            # Increment counter for each tweet processed
            i = i+1

            username = tweet.user.screen_name
            description = tweet.user.description
            location = tweet.user.location
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count
            retweetcount = tweet.retweet_count
            hashtags = tweet.entities['hashtags']

            # Check for retweets
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:
                text = tweet.full_text

            # Convert hashtag data to list
            hashtext = list()
            for tag in range(0,len(hashtags)):
                hashtext.append(hashtags[tag]['text'])

            # Append formatted data to Data Frame
            newEntry = [username, description, location, following,
                        followers, totaltweets, retweetcount, text, hashtext]
            self.tweetData.loc[len(tweetData)] = newEntry

        # Output tweet count
        print("Number of scraped tweets: %d" , (i))

    def CollectTweets(keyPath="Twitter Keys"):
        # Retrieve Twitter dev keys from file (Key file excluded from git)
        with open(keyPath,'r') as keyFile:
            isLabel = True
            keyArray = []

            # Iterate through file and recover keys
            for line in keyFile:
                if isLabel:
                    print("Retrieving " + line)
                else:
                    keyArray.append(line.rstrip("\n"))
                isLabel = not(isLabel)

        if debug:
            print(keyArray)

        # Assign keys to respective variables
        [consumer_key,consumer_secret,bearer_key,access_key,access_secret] = keyArray

        if debug:
            print(consumer_key)
            print(access_secret)

        # Set Twitter Access
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        #TODO - Reconfigure this to take external options
        # Enter Hashtag and initial date
        print("Enter Twitter HashTag to search for")
        words = input()
        print("Enter Date since The Tweets are required in yyyy-mm--dd")
        date_since = input()

        #TODO - Reconfigure to dynamically set number based on remaining pulls in
        #   the month.
        # number of tweets you want to extract in one run
        numtweet = 100

        TweetScrape(words, date_since, numtweet)
        print('Scraping has completed!')



if __name__ == '__main__':
    debug = True
    CollectTweets()
