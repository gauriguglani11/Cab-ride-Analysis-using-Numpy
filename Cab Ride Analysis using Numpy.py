#!/usr/bin/env python
# coding: utf-8

# In[125]:


import numpy as np


# In[126]:


taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header = True)


# In[127]:


#what is the mean speed of all the cab rides
speed = taxi[:, 7]/(taxi[:, 8]/3600)
#now we have trip length in hrs and then speed is in miles/hr


# In[128]:


mean_speed  = np.mean(speed)
print(mean_speed)


# #so the above is the asnwer of mean speed

# In[129]:


#Number of rides taken in february
rides_feb = taxi[taxi[:, 1] == 2]
print(rides_feb.shape[0])


# In[130]:


#Number of rides where tip more than $50
rides_tip = (taxi[taxi[:, -3] >50, -3].shape[0])
print(rides_tip)


# In[131]:


#calculate the number of rides where drop was JFK airport
#drop at JFK airport will be checked by drop location = 2
no_of_rides_JFK = taxi[taxi[:, 6] == 2, 6].shape[0]
print(no_of_rides_JFK)


# In[132]:


#max tolls amount 
maximum_tolls =  np.max(taxi[:, 11])
print(maximum_tolls)


# In[133]:


#min tolls amount 
minimum_tolls =  np.min(taxi[:, 11])
print(minimum_tolls)


# In[134]:


#Finding the unique pickup locations code
unique_pincode = np.unique(taxi[:, 6])
print(unique_pincode)


# In[135]:


#finding variance of speed
var_speed = np.var(speed)
print(var_speed)


# In[136]:


#sorting fare amount in ascending order
sort_fare_amount = np.sort(taxi[:, 9])
print(sort_fare_amount)


# In[137]:


#knowing the shape of sort_fare_amount
print(np.shape(sort_fare_amount))


# In[138]:


#searching 21 in trip_distance
search_distance = np.where(taxi[:, 7] == 21)
print(search_distance)


# #the above search function "where" gives the output the indexes where the value which we need is situated.
