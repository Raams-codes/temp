#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd

# In[]:

st.header("Pollution prediction portal")

name=st.text_input("Enter your Name")


# In[ ]:
city=st.selectbox(label="Select City", options=["Delhi","Patna","Visakhapatnam","Chandigarh"],key=[1,2,3,4])

if st.button("Predict"):
    st.write(f'Hello {name}')
    if city=="Delhi":
        pickle_delhi = open("classifier.pkl","rb")
        delhi_VAR=pickle.load(pickle_delhi)
        result = delhi_VAR.forecast(y=lagged_values,steps=7)
        st.success(f"result is{result}")
