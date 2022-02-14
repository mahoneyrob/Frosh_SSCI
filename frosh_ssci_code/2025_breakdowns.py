#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load 
data = "ssci2025.csv"


# Read the Data
all_df = pd.read_csv(data)
all_df.head()


# In[2]:


all_df['tested'] = all_df['tested'].fillna(0)
all_df.head()


# In[3]:


all_df[(all_df['tested'] == 1) & (all_df['course'] == 211) & (all_df['avg'] >= 90)]


# In[4]:


all_df.describe()


# In[5]:


bins = np.arange(40, 120, 10)
bins


# In[6]:


bins = bins.tolist()


# In[7]:


bins


# In[8]:


groups = pd.cut(all_df['avg'], bins)
groups


# In[9]:


all_df['groups'] = groups
all_df.head()


# In[10]:


rhet = all_df[all_df['course'] == 115]
rhet = rhet.groupby('groups').count()
rhety = rhet['avg'].tolist()
histnt = all_df[(all_df['course'] == 211) & (all_df['tested'] == 0)]
histnt = histnt.groupby('groups').count()
histnty = histnt['avg'].tolist()
histyt = all_df[(all_df['course'] == 211) & (all_df['tested'] == 1)]
histyt = histyt.groupby('groups').count()
histyty = histyt['avg'].tolist()


# In[11]:


xbin = [40, 50, 60, 70, 80, 90, 100]
xplus = [x+2 for x in xbin]
xminus = [x-2 for x in xbin]


# In[13]:


plt.figure(figsize = (20, 20))
plt.bar(xplus, rhety, width = 2, color = 'b', align = 'center', label = 'Rhetoric')
plt.bar(xbin, histnty, width = 2, color = 'r', align = 'center', label = 'History')
plt.bar(xminus,histyty, width = 2, color = 'g', align = 'center', label = 'History Tested')
plt.title('2025 score on HSPT to class', fontsize = 20)
plt.xlabel("Score on HSPT", fontsize = 20)
plt.ylabel("Count of students in class", fontsize = 20)

plt.grid(True)
plt.legend()
lgnd = plt.legend(fontsize = '16', mode = 'Expanded', scatterpoints = 1, loc = 'best', title = 'course', title_fontsize = '20')
plt.savefig('2025 score on HSPT to class.png')


# In[15]:


print(rhety)
print(histnty)
print(histyty)
print(xbin)
print(xplus)
print(xminus)


# In[17]:


xbin[0]


# In[ ]:




