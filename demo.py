#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import packages and test log grabbing with grok

from pygrok import Grok
import pandas as pd
import numpy as np
text = '108.28.249.14 - - [27/Apr/2023:18:49:00 +0000] "GET /images/executive-members/etosgpvkce2b0fc9904330b616e4.jpeg HTTP/2.0" 499 0 "https://rspnepal.org/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"'
pattern = '\A%{IP:ip} - - \[%{HTTPDATE:timestamp}\] "%{WORD:method} %{URIPATHPARAM:path} %{URIPROTO:protocol}/%{NUMBER:version}" %{NUMBER:response_code} %{NUMBER:content_length} "%{GREEDYDATA:referrer}" "%{GREEDYDATA:user_agent}"'
grok = Grok(pattern)
print(grok.match(text))


# In[37]:


# Cheking for logs converting an entire log file into json

f = open("oa_access.log", "r")
json = open("test.json","w")
for x in f:
    a = grok.match(x)
    json.write(str(a))
    json.write("\n")
json.close()
f.close()



# In[53]:




# In[62]:


import json
data = {'ip':[],
        'timestamp':[],
        'method':[],
        'path':[],
        'protocol':[],
        'version':[],
        'response_code':[],
        'content_length':[],
        'referrer':[],
        'user_agent':[]
       }



f = open("oa_access.log1", "r")
c=0
for x in f:
    a = grok.match(x)
    try:
        for i in a:
            data[i].append(a[i])
    except TypeError:
        c = c+ 1
        continue
print(data)
print("totol none value detected is " + str(c))
 

        
  



# In[67]:


df = pd.DataFrame(data)
df


# In[ ]:





# In[ ]:





# In[ ]:




