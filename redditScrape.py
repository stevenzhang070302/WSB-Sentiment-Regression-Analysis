#import my packages

import praw
import pandas as pd


# Acessing the reddit api

reddit = praw.Reddit(client_id="",      # your client id
                     client_secret="",  #your client secret
                     user_agent="", #user agent name
                     username = "",     # your reddit username
                     password = "")     # your reddit password
sub = ['wallstreetbets']  # make a list of subreddits you want to scrape the data from

for s in sub:
    
    subreddit = reddit.subreddit(s)   # Chosing the subreddit

#create a dictionary to store keywords


# SCRAPING CAN BE DONE VIA VARIOUS STRATEGIES {HOT,TOP,etc} we will go with keyword strategy i.e using search a keyword
    query = ['GME']

    for item in query:
        post_dict = {
            "title" : [],   #title of the post
            "score" : [],   # score of the post
            "score ratio" : [],   # upvote ratio of the post
            "id" : [],      # unique id of the post
            "url" : [],     #url of the post
            #"comms_num": [],   #the number of comments on the post
            "created" : [],  #timestamp of the post
            #"body" : []         # the descriptionof post
        }
        comments_dict = {
            "comment_id" : [],      #unique comm id
            "comment_parent_id" : [],   # comment parent id
            "comment_body" : [],   # text in comment
            "comment_link_id" : []  #link to the comment
        }
        for submission in subreddit.search(query,sort = "hot",limit = 10):
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.score)
            post_dict["score ratio"].append(submission.upvote_ratio)
            post_dict["id"].append(submission.id)
            post_dict["url"].append(submission.url)
            #post_dict["comms_num"].append(submission.comms_num)
            post_dict["created"].append(submission.created_utc)
            #post_dict["body"].append(submission.body)
            
            ##### Acessing comments on the post
            submission.comments.replace_more(limit = 1)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)
        
        post_comments = pd.DataFrame(comments_dict)

        post_comments.to_csv(s+"_comments_"+ item +"subreddit1.csv")
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(s+"_"+ item +"subreddit1.csv")