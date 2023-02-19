# Using Sentiment Analysis to identify Patterns in GME Stock from r/WallStreetBets subreddit
Using Python pandas, scikit-learn, and matplotlib to predict the relationship between r/Wallstreetbets sentiment and stock prices.

* This is a group project for the University of Georgia's CSCI 3360(Data Science 1) class.

Authors:
  - Thomas Burlingame-Smith, University of Georgia
  - Felix Luu, University of Georgia
  - Steven Zhang, University of Georgia

# Project Overview
We webscrapped Reddit comments/posts and performed a series of machine learning models such as ridge regression and Bayesian to discover the relationship of the data. The first step was data collection. At the time there were no readily avaliable datasets online via Kaggle or other sources. We had to webscrape Reddit posts for data to create a CSV file. In our repo, we can see the following files [CommentsScrape.py](https://github.com/stevenzhang070302/WSBSentimentDataScience/blob/main/CommentsScrape.py), [PostScrape.py](https://github.com/stevenzhang070302/WSBSentimentDataScience/blob/main/PostScrape.py), [redditScrape.py](https://github.com/stevenzhang070302/WSBSentimentDataScience/blob/main/redditScrape.py) as our web scrapers that created our Reddit Post Data set. They utilized Reddit's PRAW API and Pushshift.io API to readily scrape Reddit Forums for Posts, Title, Upvotes, Comment information. Additionally, we scrapped Yahoo Finance via [yahooFinance.py](https://github.com/stevenzhang070302/WSBSentimentDataScience/blob/main/yahooFinance.py) to get corresponding Stock data for GME, our stock of interest.

Now that we have CSV datasets we have to do some data preprocessing and data cleaning. See, [WSB Parser.ipynb](https://github.com/stevenzhang070302/WSBSentimentDataScience/blob/main/WSB%20Parser.ipynb) where we implemented simple preprocessing by counting specific instances of where WSB lingo ocurred indicating good or bad sentiment for associated Stock in the post. 

In [Regression.ipynb](https://github.com/stevenzhang070302/WSBSentimentDataScience/blob/main/Regression.ipynb), we performed Regression analysis on our datasets to find if there were any underlying patterns between Reddit Sentiment and corresponding GME stock price.

We used the following Classical Machine Learning Regression Models:
 - Ridge Regression
 - Random Forest
 - Bayesian
 - PLS
 - Passive Agressive


# Our Research Paper *<Please Click>*
[r/WallStreetBets Sentiment Analyzer](https://drive.google.com/file/d/1VkaRAKsLlO3ebpmFYt-b72TsTpt4QN60/view)


