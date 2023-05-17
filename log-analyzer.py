#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import the package
from pygrok import Grok
#text to be processed
text = '108.28.249.14 - - [27/Apr/2023:18:49:00 +0000] "GET /images/executive-members/etosgpvkce2b0fc9904330b616e4.jpeg HTTP/2.0" 499 0 "https://rspnepal.org/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"'
#pattern which you want to match
pattern = '\A%{IP:ip} - - \[%{HTTPDATE:timestamp}\] "%{WORD:verb} %{URIPATHPARAM:path} %{URIPROTO:protocol}/%{NUMBER:version}" %{NUMBER:response_code} %{NUMBER:content_length} "%{GREEDYDATA:referrer}" "%{GREEDYDATA:user_agent}'
#create a GROK object by giving the pattern
grok = Grok(pattern)
#use match function to get all the parsed patterns
print(grok.match(text))


# In[ ]:





# In[12]:


f = open("oa.log", "r")
json = open("test.json","w")
for x in f:
    a = grok.match(x)
    print(str(a))
    json.write(str(a))
    json.write("\n")
json.close()
f.close()


# In[ ]:





# In[ ]:




