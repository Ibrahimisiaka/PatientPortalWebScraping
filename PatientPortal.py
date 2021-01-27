#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python Algorithm that finds website with the format https://12693.portal.athenahealth.com/ and run through the different variations of that and then pulls the practice name on the site into an excel file


# In[37]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[38]:


def get_clinic_name(clinic_id):
    url         = f'https://{clinic_id}.portal.athenahealth.com/'
    response    = requests.get(url)
    html        = response.text
    soup        = BeautifulSoup(html, 'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    return clinic_name


# In[53]:


start = 12690
end   = 12710


# In[54]:


master_list = []

for clinic_id in range(start, end+1):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict['clinic_name'] != 'Payment Confirmation' and data_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address.":
        master_list.append(data_dict)
        print(clinic_id)


# In[56]:


df = pd.DataFrame(master_list)


# In[59]:


df.to_csv('clinic_data.csv', index=False)


# In[60]:


df


# In[ ]:





# In[ ]:




