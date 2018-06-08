import tweepy
import time 
import json
import pandas as pd
import numpy as np
from textblob import TextBlob
import re
import paralleldots
import csv
from paralleldots import set_api_key, get_api_key


# In[2]:


set_api_key('YAfV3gmttOytrwlxaRoH2LT2zDHPcnX2RkhvkCHEwLU')


# In[3]:


get_api_key()


# In[9]:


from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang_keywords, abuse


# In[10]:


def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# In[11]:


Tweets = pd.read_csv('tweets.csv')


# In[12]:


for t in Tweets.text:
    clean_tweet(t)


# In[13]:


print(paralleldots.sentiment(t))


# In[14]:


print(Tweets.text)


# In[15]:


print(paralleldots.sentiment(Tweets.text))


# In[16]:


sentiments = []
sentiment_score = []
tweet_list = []


# In[17]:


for _,tweet in Tweets.iterrows():
    dict_obj = paralleldots.sentiment(tweet.text)
    print(dict_obj)
    sentiments.append(dict_obj['sentiment'])
    sent = dict_obj['sentiment']
    if(sent=='neutral'):
        sentiment_score.append(dict_obj['probabilities']['neutral'])
    if(sent=='positive'):
        sentiment_score.append(dict_obj['probabilities']['positive'])
    if(sent=='negative'):
        sentiment_score.append(dict_obj['probabilities']['negative'])
    tweet_list.append(tweet.text)


# In[18]:


df = pd.DataFrame(columns=['sentiment','tweets','sentiment_score'])


# In[19]:


df['sentiment'] = sentiments
df['tweets'] = tweet_list
df['sentiment_score'] = sentiment_score


# In[21]:


df.to_csv('output.csv')

