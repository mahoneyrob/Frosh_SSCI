#!/usr/bin/env python
# coding: utf-8

# In[70]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load 
data = "all.csv"
avg = "avg.csv"

# Read the Data
all_df = pd.read_csv(data)
avg_df = pd.read_csv(avg)


# In[71]:


RDNP_211 = all_df[all_df['test_code'] == 'RDNP']
RDNP_211 = RDNP_211[RDNP_211['course'] == 211]
RDNP_211.head()
RDNP_115 = all_df[all_df['test_code'] == 'RDNP']
RDNP_115 = RDNP_115[RDNP_115['course'] == 115]
RDNP_115.head()


# In[72]:


RDNP115x = RDNP_115['hspt_score']
RDNP115y = RDNP_115['grade_percent']
RDNP_211x = RDNP_211['hspt_score']
RDNP_211y = RDNP_211['grade_percent']
rhet_ave_score = RDNP115x.mean()
rhet_ave_score
hist_ave_score = RDNP_211x.mean()
hist_ave_score
yvals = np.arange(0, 120, 1)
yvals
hx = []
rx = []
for x in range(len(yvals)):
    hx.append(hist_ave_score)
    rx.append(rhet_ave_score)


# In[74]:


plt.figure(figsize = (20, 20))
plt.scatter(RDNP115x, RDNP115y, c = 'blue', alpha = 0.8, edgecolor="black", label = 'Rhetoric')
plt.scatter(RDNP_211x, RDNP_211y, c = 'red', alpha = 0.8, edgecolor="black", label = 'History')
plt.plot(rx, yvals, c = 'blue')
plt.plot(hx, yvals, c = 'red')
plt.title('Percent in class vs score on HSPT - RDNP', fontsize = 14)
plt.xlabel("Score on HSPT", fontsize = 12)
plt.ylabel("Percent in Class", fontsize = 12)
plt.grid(True)
plt.legend()
plt.ylim([40, 120])
plt.text((hist_ave_score - 5), -3, f'History Avg: {hist_ave_score:.2f}')
plt.text((rhet_ave_score - 5), -3, f'Rhetoric Avg: {rhet_ave_score:.2f}')
lgnd = plt.legend(fontsize = '20', mode = 'Expanded', scatterpoints = 1, loc = 'best', title = 'course')
plt.savefig('Percent_in_class_vs_score_HSPT_RDNP.png')


# In[66]:


avg_211 = avg_df[avg_df['course'] == 211]
avg_211.head()
avg_115 = avg_df[avg_df['course'] == 115]
avg_115.head()


# In[67]:


avg115x = avg_115['avg_hspt_score']
avg115y = avg_115['avg_grade_percent']
avg_211x = avg_211['avg_hspt_score']
avg_211y = avg_211['avg_grade_percent']
avg_rhet_ave_score = avg115x.mean()
avg_rhet_ave_score
avg_hist_ave_score = avg_211x.mean()
avg_hist_ave_score
yvals = np.arange(0, 120, 1)
yvals
avg_hx = []
avg_rx = []
for x in range(len(yvals)):
    avg_hx.append(avg_hist_ave_score)
    avg_rx.append(avg_rhet_ave_score)
print(avg_hist_ave_score)
print(avg_rhet_ave_score)


# In[69]:


plt.figure(figsize = (20, 20))
plt.scatter(avg115x, avg115y, c = 'blue', alpha = 0.8, edgecolor="black", label = 'Rhetoric')
plt.scatter(avg_211x, avg_211y, c = 'red', alpha = 0.8, edgecolor="black", label = 'History')
plt.plot(avg_rx, yvals, c = 'blue')
plt.plot(avg_hx, yvals, c = 'red')
plt.title('Percent in class vs score on HSPT - Average', fontsize = 20)
plt.xlabel("Average Score on HSPT", fontsize = 12)
plt.ylabel("Percent in Class", fontsize = 12)
plt.grid(True)
plt.legend()
plt.ylim([40, 120])
plt.text((avg_hist_ave_score - 5), -3, f'History Avg: {avg_hist_ave_score:.2f}')
plt.text((avg_rhet_ave_score - 5), -3, f'Rhetoric Avg: {avg_rhet_ave_score:.2f}')
lgnd = plt.legend(fontsize = '20', mode = 'Expanded', scatterpoints = 1, loc = 'best', title = 'course')
#plt.savefig('Percent_in_class_vs_score_HSPT_Average.png')


# In[ ]:




