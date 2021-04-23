#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
from matplotlib.pyplot import figure


# In[56]:


gme = pd.read_csv('GME_2021-01-01-2021-02-01.csv')
del gme['Adj Close']
gme.head()


# In[57]:


difference = {}
for index, row in gme.iterrows():
    date = datetime.strptime(row['Date'], '%Y-%m-%d').date()
    date = '{:%m-%d}'.format(datetime.strptime(str(date), '%Y-%m-%d'))
    change = row['Close'] - row['Open']
    
    if date in difference:
        difference[date] = change
    else:
        difference[date] = 0
        difference[date] = change


# In[58]:


for key, value in difference.items():
    print(key, value)


# In[77]:


x, y = zip(*sorted(difference.items()))
plt.figure(figsize=(20,10))
plt.plot(x, y)
plt.show()

