#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymongo')


# In[2]:


from pymongo import MongoClient 


# In[3]:


client=MongoClient("mongodb://localhost:27017/")


# In[4]:


db=client['Task']


# In[5]:


my_collection=db['Telephone']


# In[6]:


#To create new collections
my_collection.insert_one({'name':'swathi','phonenumber':'2439723545','place':'chennai'})


# In[7]:


client.list_database_names()


# In[8]:


db.list_collection_names()


# In[9]:


#To insert multiple records
my_collection.insert_many([{'name':'santhosh','phonenumber':'24685225455','place':'mysore'},{'name':'siva','phonenumber':'25654235458','place':'pune'},{'name':'uma','phonenumber':'24967521452','place':'delhi'},{'name':'shyam','phonenumber':'2654789321','place':'goa'},{'name':'simba','phonenumber':'24672548555','place':'chennai'}])


# In[10]:


#To Read collections
myquery = { "place": "chennai" }
for i in my_collection.find(myquery):
    print(i)


# In[11]:


#To Update Collections
Q={'place':'pune'}
new={'$set':{'name':'sivakumar'}}


# In[12]:


my_collection.update_one(Q,new)
  


# In[13]:


for i in my_collection.find({'place':'pune'}):
    print(i)


# In[14]:


for i in my_collection.find():
    print(i)


# In[15]:


#To delete collection
my_collection.delete_one({'name':'swathi'})


# In[16]:


for i in my_collection.find():
    print(i)

