#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
l=[2,3,4,5]
print(l)
print(type(l))


# In[3]:


#creating a numpy array
a=np.array([12,2,4])
print(a)
print(type(a))


# In[4]:


#attributes of numpy array
#1
#np.arr.ndim
#which returns the dimensions of the array
#first create the array and print the dimension of the array
a.ndim


# In[8]:


b=np.array([[1,3,4,5],[3,4,5,6]])
print(b)
print("The dimension of the array")
print(b.ndim)
print("The shape of the array returns the row size and column size")
print(b.shape)
print("The size of the array,returns the no. of elements in the array")
print(b.size)
print("To rteurn the dtype of the array")
print(b.dtype)


# In[9]:


print("Inorder to return all zeros in sprcified row and column")
c=np.zeros(7)
print(c)


# In[11]:


d=np.zeros((3,5),)
print(d)


# In[13]:


d=np.zeros((3,5),dtype=int)
print(d)
print("lly for ones")


# In[14]:


print("Reshapr and Random Number Generator")
print("Use np.radom.random")


# In[15]:


print("Use of arange function")
k=np.arange(4)
print(k)

