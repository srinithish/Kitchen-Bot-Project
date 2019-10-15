# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:41:57 2019

@author: GELab
"""

import speech_recognition as sr
import re
import voiceFeedback
import queue
import time

class Action():
    
    def __init__(self,verb,obj):
        
        self.verb = verb
        self.object = obj
        
        
    def send():
        
        
        pass
    
    def __repr__(self):
        
        return 'action: {}   and   object: {}'.format(self.verb,self.object)
        
    def __eq__(self,other):
        
        return self.verb == other.verb and self.object == other.object
    
    
    
    


def triggerHotWord(recognizer, audio):                          # this is called from the background thread
    try:
        
        
        text = r.recognize_google(audio)
        print("You said " + text)  # received audio data, now need to recognize it
        
        m = re.match("(?:Hello|Hey) robot", 
                         text,re.IGNORECASE)
            
            
        if m.group().lower() == 'hello robot' or m.group().lower() == 'hey robot':
            
                
            voiceFeedback.playClip('./audioCaptures/whatsUp.mp3')
            return True
        
        
    except Exception as e:
        print(e)
        print("Oops! Didn't catch that")
        return False
        
    
class customListener():
    
    
    def __init__(self,actionList):
        
        self.commandQueue = queue.Queue()
        self.possibleActions = actionList
        
        pass
        
    def parseSpokenText(self,recognizer, audio):
            ## define all possible actions
                       
            
            try: 
    #            text = r.recognize_sphinx(audio) 
                text = recognizer.recognize_google(audio) 
                print ("you said: " ,text)
    #            m = re.match("(?:Hello|Hey).*(?:robot|bot).*(?:get|give).*me (.*)", 
    #                         text,re.IGNORECASE)   
                
    #            m = re.match("(?:Hello|Hey) robot (?P<verb>.*) me a (?P<object>.*)", 
    #                         text,re.IGNORECASE)
                
                
                m = re.match("(?:Hello|Hey) robot (?P<verb>.*) me (?P<object>.*)", 
                             text,re.IGNORECASE)
                
    #            print(m.group('verb'),'  ',m.group('object'))
                commandedAction = Action(m.group('verb'),m.group('object'))
                
                if commandedAction in self.possibleActions:
                    print (commandedAction)
                    voiceFeedback.playClip('./audioCaptures/gotIt.mp3')
                    
                    self.commandQueue.put(commandedAction)
                    
                    return commandedAction
                
                
                else:
                    print('matched the pattern but not recognised command')
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



if __name__ == '__main__':
    
    """
    repo : https://github.com/srinithish/Kitchen-Bot-Project
    usage python threadedSpeechRecognition.py
    """
    
    ## create action list
    makeNoodles = Action('make','noodles')
    possibleActions = [makeNoodles]
    
    listener = customListener(possibleActions)
    r = sr.Recognizer()
    source  = sr.Microphone()
    stopper = r.listen_in_background(source,listener.parseSpokenText,phrase_time_limit=6) ### returns stopper
    
    
    ##main therad keeps active the backgroound thread

    while True: 
        time.sleep(0.1)
        if listener.commandQueue.empty() == False:
            stopper()
            ## call the robot start
            print('start the task')
            break