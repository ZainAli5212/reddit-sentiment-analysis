import pandas as pd
from textblob import TextBlob
from data_cleaner import file_path, script_dir
from textblob.exceptions import MissingCorpusError


# df.drop("comments", axis=1, inplace=True)
# df.dropna(subset=['cleaned_comments'], inplace=True)

import os

def get_sentiment(text):
    """
    Analyzes the sentiment of a given text using TextBlob.
    
    The TextBlob `sentiment.polarity` value ranges from -1 (very negative) to +1 (very positive).
    We use these values to classify the sentiment.
    
    - Polarity > 0: Positive
    - Polarity < 0: Negative
    - Polarity == 0: Neutral
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        str: The sentiment classification ('Positive', 'Negative', or 'Neutral').
    """
    if pd.isna(text) or text.strip() == "":
        return 'Neutral'

    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    """
    Main function to perform sentiment analysis.
    """
    # --- Step 1: Read the cleaned data file ---
    # IMPORTANT: Update the filename to match the one you created

    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded cleaned data from {file_path}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found in the directory: {script_dir}")
        print("Please make sure you have run the data_preprocessing.py script first.")
        return

    # --- Step 2: Perform sentiment analysis ---
    print("\n--- Starting Sentiment Analysis ---")
    
    try:
        # Apply the sentiment analysis function to the 'cleaned_comment' column
        df['sentiment'] = df['cleaned_comments'].apply(get_sentiment)
        
        # Display the first 10 rows with the new 'sentiment' column
        print("\nComments with Sentiment (First 10 Rows):")
        print(df[['comments', 'sentiment']].head(10))

    except MissingCorpusError:
        print("\nError: TextBlob's required corpora are missing.")
        print("Please run 'python -m textblob.download_corpora' in your terminal and then re-run this script.")
        return

    # --- Step 3: Summarize and save the final dataset ---
    print("\n--- Project Summary ---")
    sentiment_counts = df['sentiment'].value_counts(normalize=True) * 100
    print("\nOverall Sentiment Distribution:")
    print(sentiment_counts.to_string())

    # final_file_name = f"{os.path.splitext(cleaned_file_name)[0]}_final.csv"
    # final_file_path = os.path.join(script_dir, final_file_name)
    
    df.to_csv(file_path, index=False)
    print(f"\nFinal data with sentiment saved to {file_path}")

if __name__ == "__main__":
    main()



