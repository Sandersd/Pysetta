# quiz.py
#Get a random question everytime you open the terminal
#NOTE: questions.txt must be formatted with question=answer (both touching equal sign)

import random

import pyvona   #For the text to speech
import os
from subprocess import call

#qa -> question/answer
qaFile = open('questions.txt') #path to your questions file

qas = qaFile.readlines()

qaFile.close()

random.shuffle(qas) #randomize list

q = qas[0].split('=')[0].rstrip()   #get question (before equal sign)
a = qas[0].split('=')[1].rstrip()   #get answer (after equal sign)

#Comment this block out if not using speech
speechFile = q + '.mp3'
v = pyvona.create_voice('Access Key', 'Secret Key') #From https://www.ivona.com
#v.speak('Hello World') #if pygame installed
v.codec = 'mp3'
v.voice_name = 'Mathieu'        #French voice
v.fetch_voice(q, speechFile)    #Save tts as mp3
call(["afplay",speechFile])     #Play mp3
os.remove(speechFile)           #Delete mp3

def run(q,a):

    print(q)            #Print question

    wrong = True

    while wrong:
        inp = input()       #Grab input
        if a == inp:        #if correct answer
            print("YAAASSS")
            wrong = False   #End loop GOTO line 49
        else:
            print('nope')   #if wrong, keep asking

while True:
    try:
        run(q,a)
        exit()              #TODO add prompt for "Another?"
    except KeyboardInterrupt:
        pass                #Don't allow CTRL-C cheating
