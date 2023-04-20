import praw
import os
from dotenv import load_dotenv

load_dotenv('deets.env')

reddit = praw.Reddit(
    client_id=os.getenv('RED_CLIENT_ID'),
    client_secret=os.getenv('RED_API_KEY'),
    password=os.getenv('RED_PASSWORD'),
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
               "Safari/537.36",
    username=os.getenv('RED_USERNAME')
)

def news2Array(sub, time, upvoteScore):
    news = {}
    subreddit = reddit.subreddit(sub)
    global j
    j = 0
    for submission in subreddit.top(time_filter=time):
        if submission.score > upvoteScore:
            news[j] = submission.title, submission.url, submission.score
        j = j + 1
    return news
