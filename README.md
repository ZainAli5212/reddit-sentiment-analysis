# Reddit Sentiment Analysis Project

## Overview
This project performs sentiment analysis on Reddit comments related to a specific topic. The goal is to determine the overall sentiment (positive, negative, or neutral) of public discussion on a given subject.

## Project Stages
This project is broken down into three main stages:
1.  **Data Collection:** Uses the Reddit API (PRAW) to collect raw comments.
2.  **Data Preprocessing:** Cleans the raw text by removing URLs, mentions, and special characters.
3.  **Sentiment Analysis:** Analyzes the sentiment of each cleaned comment using the TextBlob library.

## How to Run the Project
1.  **Get Reddit API Credentials:** Follow the instructions in the `data_collector.py` file to get your own Client ID and Client Secret.
2.  **Install Dependencies:** Run `pip install praw pandas textblob`.
3.  **Run the Scripts in Order:**
    * `python data_collector.py`
    * `python data_preprocessing.py`
    * `python model.py`

## Technologies Used
-   **Python**
-   **PRAW** (Python Reddit API Wrapper)
-   **Pandas**
-   **TextBlob**
