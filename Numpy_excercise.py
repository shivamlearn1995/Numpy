#!/usr/bin/env python
# coding: utf-8

# # What is the average height of US Presidents?

# In[6]:


import numpy as np
import pandas as pd
dt=pd.read_csv("https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/president_heights.csv")
dt.head() # to know the values of data frames by default it shows upto five column. 


# In[7]:


heights=np.array(dt['height(cm)'])
print(heights,end=" ")


# In[20]:


#Summary of data
print("Mean height of the president :",heights.mean())
print("Standard deviation of heights data :",heights.std())
print("Maximum heights among president :",heights.max())
print("Minimum heights among president :",heights.min())


# In[12]:


print("25 percentile :",np.percentile(heights,25))
print("Median :",np.median(heights))
print("75 percentile :",np.percentile(heights,75))


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


# In[18]:


plt.hist(heights)
plt.title("Height Distribution of the US Presidents")
plt.xlabel("Height(CM)")
plt.ylabel("number")
plt.show()


# # End

# In[21]:


get_ipython().system('pip install pandoc')


# In[ ]:




