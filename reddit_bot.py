import praw
user_agent = ("Reddit_Python 0.1")


r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("learnpython")
for submission in subreddit.get_hot(limit = 5):
    print ("Title: ", submission.title)
    print (" Score: ", submission.score)
    print ("------------\n")
