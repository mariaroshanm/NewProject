#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

with open("Global-superstore.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)


# In[20]:


import pandas as pd
data = pd.read_csv('Global-superstore.csv', encoding= 'unicode_escape')


# In[21]:


print(data)


# In[23]:


data.isnull()


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


plt.plot()


# In[13]:


import pandas as pd
data = pd.read_csv('Global-superstore.csv', encoding= 'unicode_escape')


# In[14]:


print(data)


# In[29]:


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Global-superstore.csv', encoding='unicode_escape')
x = df['Category']
y = df['Sales']
plt.xlabe=('Category')
plt.ylable=('Sales')
plt.bar(x,y)
plt.show()


# In[10]:


import pandas as pd
df = pd.read_csv('Global-superstore.csv', encoding='unicode_escape')
df.plot.scatter(x='Sales', y='Profit')


# In[14]:


import pandas as pd
df = pd.read_csv('Global-superstore.csv', encoding='unicode_escape')
df.plot(x='Country', y='Sales')

