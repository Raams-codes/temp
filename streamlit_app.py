#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st


# In[7]:


st.write("Hello World")


# In[ ]:
st.selectbox(label="Select City", options=["Delhi","Patna","Visakhapatnam","Chandigarh"])

st.text_input("Enter City Name")

# In[ ]:


# In[ ]:

if st.button("Submit"):
  write("Hi we are processing")


