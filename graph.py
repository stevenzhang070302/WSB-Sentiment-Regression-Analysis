# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 08:37:07 2021

@author: tburl
"""
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


labels = ['Ridge','Random Forest','Bayesian','PLS', 'Passive Aggressive']
number_comments_scores = [.1719 ,-.0317, .1717, .1719,.4998]
sentiment_scores = [-.0605, .7832, -.0605, -.0605, -.5696]

x = np.arange(len(labels))  
width = .35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,number_comments_scores , width, label='Number of Comments')
rects2 = ax.bar(x + width/2, sentiment_scores, width, label='Sentiment Score')


ax.set_ylabel('Scores')
ax.set_title('Scores by Regression Model')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.plot()
plt.axhline(0, color='black')

