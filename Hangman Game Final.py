# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:00:28 2021

@author: MANSI
"""

import random

def word_selected():
    word_file = open('C:/Users/MANSI/Downloads/hang.txt','r+')
    word = random.choice(word_file.read().split())
    word_file.close()
    return word
   
def play(word):
    guesses=[]
    tries=6
    done=False
    while(done==False):
        print(display_hangman(tries))
        guess=input("Guess a letter: ").lower()
        guesses.append(guess)
        for letter in word:
           if letter  in guesses:
               print(letter,end=" ")
           else:
               print("_",end=" ")
               
        print("")       
        if guess not in word:
            tries=tries-1
            if tries==0:
                break
        done=True
        for letter in word:
            if letter not in guesses:
                done=False
                
    if (done==True):
        print("You Got it right! The word is ",word)
    else:
        print("You lose, the word was ",word)   

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    //|\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

#welcoming the user
name = input("What is your name? ")
print ("Hello, " + name, "Let's play hangman!")

word = word_selected()
print(f"You got a {len(word)} letter word")
play(word)
while input("Do u wanna try again? (Y/N) ").upper() == "Y":
    word = word_selected()
    print(f"You got a {len(word)} letter word")
    play(word)