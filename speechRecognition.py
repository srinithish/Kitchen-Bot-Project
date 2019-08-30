#Python 2.x program for Speech Recognition 
  
import speech_recognition as sr 
import re
import voiceFeedback


class Action():
    
    def __init__(self,verb,obj):
        
        self.verb = verb
        self.object = obj
        
        
    def send():
        
        
        pass
    
    def __repr__(self):
        
        return 'action is : {} and object is : {}'.format(self.verb,self.object)
        
    def __eq__(self,other):
        
        return self.verb == other.verb and self.object == other.object
        
        
#enter the name of usb microphone that you found 
#using lsusb 
#the following name is only used as an example 
mic_name = "Microphone (UM02)"
#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 
  
#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 
  
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
  
#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 
        
def triggerHotWord():
    
    with sr.Microphone(device_index= 2,sample_rate = sample_rate,  
                            chunk_size = chunk_size) as source:
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source) 
        print("Say the hotword")
        #listens for the user's input 
        
        
        try: 
            audio = r.listen(source,phrase_time_limit=2) 
            text = r.recognize_google(audio) 
            print ("you said: " ,text)
#            m = re.match("(?:Hello|Hey).*(?:robot|bot).*(?:get|give).*me (.*)", 
#                         text,re.IGNORECASE)   
            
            m = re.match("(?:Hello|Hey) robot", 
                         text,re.IGNORECASE)
            
            
            if m.group().lower() == 'hello robot' or m.group().lower() == 'hey robot':
                
                    
                voiceFeedback.playClip('./audioCaptures/whatsUp.mp3')
                return True

        
        except Exception as e :
        
            print(e)
            return False
    
def parseSpokenText(possibleActions):
    
    
    
    with sr.Microphone(sample_rate = sample_rate,  
                            chunk_size = chunk_size) as source:
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source) 
        print("Now tell me the action")
        #listens for the user's input 
        
        
        try: 
            audio = r.listen(source,phrase_time_limit=6) 
            text = r.recognize_google(audio) 
            print ("you said: " ,text)
#            m = re.match("(?:Hello|Hey).*(?:robot|bot).*(?:get|give).*me (.*)", 
#                         text,re.IGNORECASE)   
            
#            m = re.match("(?:Hello|Hey) robot (?P<verb>.*) me a (?P<object>.*)", 
#                         text,re.IGNORECASE)
            
            
            m = re.match("(?P<verb>.*) me a (?P<object>.*)", 
                         text,re.IGNORECASE)
            
#            print(m.group('verb'),'  ',m.group('object'))
            commandedAction = Action(m.group('verb'),m.group('object'))
            
            if commandedAction in possibleActions:
                print (commandedAction)
                return commandedAction
            
            
            else:
                ## matched the pattern but not recognised command 
                raise AttributeError
                    
            
            
        #error occurs when google could not understand what was said 
          
#        except sr.UnknownValueError as e: 
#            print("Google Speech Recognition could not understand audio") 
#            
#        
#        except sr.WaitTimeoutError:
#            print("Google Speech Recognition timeout error") 
#            
#            
#        
#        except sr.RequestError as e: 
#            print("Could not request results from Google\
#                                     Speech Recognition service {}".format(e)) 
        
        
        except AttributeError:
            ###not mathing the pattern at all
            print('Not a recognised command')
            voiceFeedback.playClip('./audioCaptures/didntGetThat.mp3')
            
        except Exception as e :
            ## all other exceptions
            print(e)
            return None
        
            
if __name__ == '__main__' :
    
    
    
    ## peeporioni
    makePepperoni = Action('make','pepperoni')
    getPepperoni = Action('get','pepperoni')
    possibleActions = [makePepperoni,getPepperoni]
#    
#    
#    
#    while True:
#        
#        returnedAction = parseSpokenText(possibleActions)
#         
#        if returnedAction is not None:
#            break



### trigger word deteaction
    
    while True:
        
        isTriggered = triggerHotWord()
        
        
        if isTriggered == True:
            
            while True:
                returnedAction = parseSpokenText(possibleActions)
                
                
                if returnedAction is not None:
                    voiceFeedback.playClip('./audioCaptures/gotIt.mp3')
                    break
    
