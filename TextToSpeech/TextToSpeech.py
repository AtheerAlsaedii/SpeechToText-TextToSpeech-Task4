# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:55:29 2021

@author: huawei-pc
"""
"""""""""""""""""""""""""""""""""""Authenticate"""""""""""""""""""""""""""""""""""

url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ab95914b-87aa-471e-b54e-105d9de29e35'
apikey = 'HHWFlbf1eRTuwrzAQ1-GhhYioG-VOPtvoWuWem5tFmre'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

"Setup service"
authenticator = IAMAuthenticator(apikey)
"New TTS Service"
tts = TextToSpeechV1 (authenticator=authenticator)
"Set Service URL"
tts.set_service_url(url)

"""""""""""""""""""""""""""""""""""Convert a String"""""""""""""""""""""""""""""""""""

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
    

"""""""""""""""""""""""""""""""""""Convert from file"""""""""""""""""""""""""""""""""""
with open('Churchill.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]  
text = ''.join(str(line) for line in text)

with open('./winston.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)
    
