# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:41:57 2019

@author: nithish
"""

import speech_recognition as sr
import re
import voiceFeedback
import queue
import time



class Action():
    
    def __init__(self,wordList,funcToExceute,priority = 1000):
        
        self.wordList = wordList
        self.function = funcToExceute
        self.priority = priority
    def send():
        
        
        pass
    
    def callFunc(self):
        
        func = self.function
        val = func()
        return val
    
    def isMatchingPhrase(self,phrase):
        
        foundWordList = re.findall('|'.join(self.wordList), phrase)
        
        if set(foundWordList) == set(self.wordList):
            
            return True
        
        else:
            
            return False
        

    def __repr__(self):
        
        return 'action: {} and function: {} '.format(self.wordList,self.function)
    
    
   
        
#    def __eq__(self,other):
#        
#        return self.verb == other.verb and self.object == other.object
    
    
    
    


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
        
        self.commandQueue = queue.PriorityQueue()
        self.possibleActions = actionList
        
        pass
    

    def addActions(self,action):
        self.possibleActions.append(action)
        
        return True
        
        
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
                
                
#                m = re.match("(?:Hello|Hey) (?P<phrase>.*)", 
#                             text,re.IGNORECASE)
                
                m = re.match("(?P<phrase>.*)", 
                             text,re.IGNORECASE)
                
    #            print(m.group('verb'),'  ',m.group('object'))
                
                phrase = m.group('phrase') ## will raise error
                
                phrase = phrase.lower()
                
                for action in self.possibleActions:
                    
                    if action.isMatchingPhrase(phrase):
                        self.commandQueue.put((action.priority,action))    
                    
                        voiceFeedback.playClip('./audioCaptures/gotIt.mp3')
                        break
                
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

def listenAndPerformActions(possibleActions):
    
    listener = customListener(possibleActions)
    r = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names() 
    
    deviceIndex= mic_list.index('Microphone (UM02)')
    source  = sr.Microphone(device_index=deviceIndex)
#    r.adjust_for_ambient_noise(source) 
    
    stopper = r.listen_in_background(source,listener.parseSpokenText,phrase_time_limit=6) ### returns stopper
    
    
    stopAction = Action(['stop','listening'],stopper)
    listener.addActions(stopAction)
    
    return listener

if __name__ == '__main__':
    
    """
    repo : https://github.com/srinithish/Kitchen-Bot-Project
    usage python threadedSpeechRecognition.py
    """
    


    ## create action list
    makeNoodles = Action(['make','noodles'],lambda: print("Sure"))
    stirAction = Action(['stir'],lambda: print("Sure"))
    pourAction = Action(['pour','water'],lambda: print("Sure"))
    switchOnStove = Action(['switch','on','stove'],lambda: print("Sure"))
    stopRobotAction = Action(['stop','moving'],lambda: print("Sure"),0)
    pauseRobotAction = Action(['pause','moving'],lambda: print("Sure"),1)
    startRobotAction = Action(['start','moving'],lambda: print("Sure"),2)
    
    
    possibleActions = [makeNoodles,stirAction,pourAction,
                       switchOnStove,stopRobotAction,pauseRobotAction]
    
    listener= listenAndPerformActions(possibleActions)
    listener.possibleActions
    ##main therad keeps active the backgroound thread

    while True: 
        time.sleep(0.1)
        if listener.commandQueue.empty() == False:
#            stopper()
            priority,action = listener.commandQueue.get()
            action.callFunc()
            ## call the robot start
            print("starting ",action)
      
    

    
