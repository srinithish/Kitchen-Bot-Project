# -*- coding: utf-8 -*-


from gtts import gTTS 
from playsound import playsound




def generateAudioClip(text,filepath):
    
    
    language = 'en'
  

    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save(filepath)
    
    
    pass
    
    
def playClip(filepath):
    
    playsound(filepath,block = True)
    
    pass


if __name__ == '__main__':
    
    generateAudioClip('Got it','./audioCaptures/gotIt.mp3')
    generateAudioClip("Hey what's up",'./audioCaptures/whatsUp.mp3')
    generateAudioClip('Sorry didnt get that.Can you say the once again','./audioCaptures/didntGetThat.mp3')
    
    
    
    
    
    
    
    
    
    