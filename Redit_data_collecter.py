# Reddit Sentiment Analysis

# praw is a Python package that allows for simple access to Reddit's API.
import praw    
import pandas as pd
import re
import textblob
import os

# Set up Reddit API credentials
CLIENT_ID = "rJRpmetATzk0MGezFZxdIw"
CLIENT_SECRET = "6NDrlLJinwjR9pEhT_V_uPaJgtGscQ"
USER_AGENT = "sentiment_analyzer/1.0"

# Authenticate with Reddit's API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT)



# Define the subreddit and search term
subreddit_name = "movies"
search_query = "How to train your dragon (2025)"
post_limit = 50  # Number of posts to fetch 

print(f"Searching for posts in r/{subreddit_name} with query '{search_query}'...")



# Fetch posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.search(search_query, limit=post_limit)



# A list to store the data we collect.
data_list = []
print(f"Fetch posts and comments... This may take a while...")


for post in posts:
    post.comments.replace_more(limit=0) # Load all comments for the post
    for comment in post.comments.list():
        # check if the commet has text and is not a more comment
        if hasattr(comment, 'body'):
            #this cleans the comment text before adding it to the list
            data_list.append(comment.body)
print(f"Successfully collected {len(data_list)} comments.")



    
