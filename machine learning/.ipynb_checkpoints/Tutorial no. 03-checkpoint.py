#!/usr/bin/env python
# coding: utf-8

# # Tutorial no.03

# **On pandas ,googleplaystore.csv datset**

# **1. Display first 5 records of the dataframe.**

# In[1]:


import pandas as pd
df=pd.read_csv('googleplaystore.csv')
df.head(5)


# **2. Display Category with highest number of apps registered.**

# In[2]:


df['Category'].value_counts()


# **3. What is the average ratings for all the apps?**

# In[3]:


df['Rating'].mean()


# **4. Total number of apps which even supports Andriod version 2.3 and up.**

# In[4]:


fi=df.query("`Android Ver` == '2.3 and up'")
len(fi)


# **5. Impute the missing values available in Content Rating column with respective measure of
# central tendency.**

# In[5]:


df['Content Rating'].isnull().value_counts()


# **On dataset salaries.xlsx**

# **1. Read the file as a dataframe called sal.**

# In[6]:


sal = pd.read_excel('salaries.xlsx')


# **2. Check the header of the DataFrame.**

# In[7]:


sal.head()


# **3. Use the .info() method to find out how many entries there are.**

# In[8]:


sal.info()


# **4. What is the average BasePay ?**

# In[9]:


sal['Salary'].mean()


# **5. What is the highest amount of OvertimePay in the dataset ?**

# In[10]:


sal[['Salary','Hours per Week']].max()


# **8. How many unique job titles are there?**

# In[11]:


sal['Workclass'].nunique()


# **9. What are the top 5 most common jobs?**

# In[14]:


sal['Occupation'].value_counts()


# In[ ]:




