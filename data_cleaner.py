import re
import pandas as pd
import os 
# Import data_list, subreddit_name, and search_query from Redit_data_collecter.py
try:
    from Redit_data_collecter import data_list, subreddit_name, search_query
except ImportError:
    data_list = []


#data cleaning function
def data_cleaning(data):
    # Remove URLs
    data = re.sub(r'http\S+|www\S+|https\S+', '', data, flags=re.MULTILINE)
    # Remove user mentions
    data = re.sub(r'\@\w+|\#\w+','', data) 
    # Remove special characters and numbers
    data = re.sub(r'[^A-Za-z\s]', '', data) 
    # Remove extra whitespace
    data = re.sub(r'\s+', ' ', data).strip()
    # removing stopwords
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',"aren't","can't",'couldn',"couldn't",'didn',"didn't",'doesn',"doesn't",'hadn',"hadn't",'hasn',"hasn't",'haven',"haven't",'isn',"isn't",'ma','mightn',"mightn't",'mustn',"mustn't",'needn',"needn't",'shan',"shan't",'shouldn',"shouldn't",'wasn',"wasn't",'weren',"weren't",'won',"won't",'wouldn',"wouldn't", ] 
    data = ' '.join([word for word in data.split() if word.lower() not in stopwords]) 
    # lowercase the text
    data = data.lower()
    
    return data

# Save the collected data to a CSV file
# Pandas is perfect for handling data. We'll put our comments into a DataFrame.

if data_list:
        df = pd.DataFrame(data_list, columns=['comments'])
        df['cleaned_comments'] = df['comments'].apply(data_cleaning)
        file_name = f"{subreddit_name}_{search_query.replace(' ', '_')}.csv"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
else:
    print("No comments were collected. Please check your query or subreddit name.")
