import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from warnings import simplefilter
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import PassiveAggressiveRegressor
import matplotlib.pyplot as plt

def wsb_stats():

    wsb = pd.read_csv('jantofebScrape.csv')
    del wsb['Post ID']
    del wsb['Title']
    del wsb['Url']
    del wsb['Author']
    del wsb['Permalink']
    del wsb['Flair']

    simplefilter(action='ignore', category=FutureWarning)

    prev = datetime.strptime('2020-01-01 00:05:21', '%Y-%m-%d %H:%M:%S').date()
    wsb_dates = []
    score_dict = {}
    comment_dict = {}
    wsb_dict = {}
    count = 0
    comments = 0
    score = 0
    for row in wsb['Publish Date']:
        date_time_str = row
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S').date()
        if(prev < date_time_obj):
            score = 0
            comments = 0
            wsb_dates.append(date_time_obj)
            prev = date_time_obj
        else:
            score += wsb['Score'][count]
            comments += wsb['Total No. of Comments'][count]
            count += 1
        wsb_dict[date_time_obj] = [score, comments]
        score_dict[date_time_obj] = score
        comment_dict[date_time_obj] = comments


    return pd.DataFrame.from_dict(wsb_dict)


def gme_stats():
     wsb = pd.read_csv('GME_2021-01-01-2021-02-01.csv').values
    
     data=[-1.75,-1.75,-1.75]
     count=0
     for i in wsb:
         if len(data)>=31:
             break
         count+=1
         data.append(i[4]-i[1])
         
         if(count==6):
             data.append(i[4]-i[1])
             data.append(i[4]-i[1])
             data.append(i[4]-i[1])
             count=0
     return pd.DataFrame.from_dict(data)

gme=gme_stats()

data=wsb_stats()

data=data.values
gme=gme.values

plt.figure(1)
plt.plot(data[0])
plt.xlabel('Days')
plt.ylabel('Sentiment')
plt.box(False)

plt.figure(2)
plt.plot(data[1])
plt.xlabel('Days')
plt.ylabel('Number of Comments')
plt.box(False)

plt.figure(3)
plt.plot(gme)
plt.xlabel('Days')
plt.ylabel('Change in Price')
plt.box(False)

"""
X_train, X_test, y_train, y_test = train_test_split(data[0],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)
print("Ridge")
alph=1
scores=[]
for i in range(100):
    clf = Ridge(alpha=alph)
    clf.fit(X_train,y_train)
    scores.append(clf.score(X_test,y_test))
    alph-=.01
print(np.mean(scores))


X_train, X_test, y_train, y_test = train_test_split(data[1],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

alph=1
scores=[]
for i in range(100):
    clf = Ridge(alpha=alph)
    clf.fit(X_train,y_train)
    scores.append(clf.score(X_test,y_test))
    alph-=.01
print(np.mean(scores))

print("Random Forest")
X_train, X_test, y_train, y_test = train_test_split(data[0],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=RandomForestRegressor(max_depth=2, random_state=0).fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))


X_train, X_test, y_train, y_test = train_test_split(data[1],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=RandomForestRegressor(max_depth=2, random_state=0).fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))

print("Bayesian Ridge")
X_train, X_test, y_train, y_test = train_test_split(data[0],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=linear_model.BayesianRidge().fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))


X_train, X_test, y_train, y_test = train_test_split(data[1],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=linear_model.BayesianRidge().fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))

print("PLS")
X_train, X_test, y_train, y_test = train_test_split(data[0],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=PLSRegression(n_components=1).fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))


X_train, X_test, y_train, y_test = train_test_split(data[1],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=PLSRegression(n_components=1).fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))

print("Passive Aggressive")

X_train, X_test, y_train, y_test = train_test_split(data[0],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=PassiveAggressiveRegressor(max_iter=100, random_state=0).fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))


X_train, X_test, y_train, y_test = train_test_split(data[1],gme, test_size=0.10, random_state=0)
X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

clf=PassiveAggressiveRegressor(max_iter=100, random_state=0).fit(X_train,y_train.ravel())
print(clf.score(X_test,y_test))
"""