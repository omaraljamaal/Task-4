#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install ibm_watson


# In[4]:


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[5]:


apikey = 3vMCt3mSKyikpsAv2YB90Zk6iXCkKGLmvDCXd98rVUai'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/8e86e67a-d7ab-41cb-8891-c3a3eb1bc874'


# In[6]:


authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


# In[8]:


with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hi I am Omar studing computer', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)


# In[ ]:




