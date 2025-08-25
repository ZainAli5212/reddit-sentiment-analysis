# Reddit Sentiment Analysis

# praw is a Python package that allows for simple access to Reddit's API.
import praw    
from prawcore.exceptions import NotFound

# Set up Reddit API credentials
CLIENT_ID = "rJRpmetATzk0MGezFZxdIw"
CLIENT_SECRET = "6NDrlLJinwjR9pEhT_V_uPaJgtGscQ"
USER_AGENT = "sentiment_analyzer/1.0"

# Authenticate with Reddit's API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT)


# All of this code should be inside the 'try' block
try:
    subreddit_name = input("Enter the subreddit name (without r/) e.g, movies: ")
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.id
    # print(f"Subreddit r/{subreddit_name} is valid.")

    search_query = input("Enter the search query e.g, Dune 2: ")
    print(f"Searching for posts in r/{subreddit_name} with query '{search_query}'...")

    post_limit = 50 
    posts = subreddit.search(search_query, limit=post_limit)

    data_list = []
    print(f"Fetch posts and comments... This may take a while...")

    for post in posts:
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            if hasattr(comment, 'body'):
                data_list.append(comment.body)
                
    print(f"Successfully collected {len(data_list)} comments.")

# The 'except' blocks should follow the 'try' block
except NotFound:
    print(f"Error: Subreddit '{subreddit_name}' not found. Please enter a valid subreddit name.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
