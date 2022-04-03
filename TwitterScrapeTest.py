import sys
import pathlib

rootPath = pathlib.Path().absolute()
handlerPath = str(rootPath) + "/Handlers"
sys.path.insert(0,handlerPath)

import TwitterHandler as th
import DatabaseHandler as dh
import sys

if __name__ == ('__main__'):

    THandler = th.TwitterHandler(rootPath)
    DBHandler = dh.DatabaseHandler()

    THandler.GetTweets()
    DBHandler.SaveToDB("Tweet Data",TwitterHandler.tweetData)
