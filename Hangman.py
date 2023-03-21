#A Hangman code with life half the length of the word which chooses a word randomly from a file

import random

#checking if the word is present or not
def checkExisting(listOfLetters,rightAns,allKey,key):
    if key in listOfLetters:
        rightAns.append(key)
        allKey.append(key)
        return True
        
    else:
        allKey.append(key)
        return False




#hangman graphic
pics=['''
=========||
         ||
         ||
         ||
         ||
         ||
         || ''',
    '''
=========||
    |    ||
         ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
    |    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   / \   ||
         ||
         || ''',
]



#declaration of var,list etc
with open('D:\py\List.txt','r') as f:
    wordsList = f.read().split("\n")

randomWord=random.choice(wordsList)
correctLetters=list(randomWord)

exisitngLetters=[]
allLetters=[]

i=int(len(randomWord)/2)


#start of main fn
print("Welcome to the hangman!")
print(pics[0])
print()
print("Your word contains "+str(len(randomWord))+" letters")
print('Life:'+str(i))
for k in correctLetters:
        print('_',end=' ')
global m 
m=1

while True:
    print()
    print('Select a Alphabet:')
    userInp=input()
    
    #checking if the input is valid or not
    boolCheck=checkExisting(correctLetters,exisitngLetters,allLetters,userInp)
    if boolCheck:
        for j in correctLetters:
            if j in exisitngLetters:
                print(j,end=' ')
            else:
                print('_',end=' ')
    else:
        for j in correctLetters:
            if j in exisitngLetters:
                print(j,end=' ')
            else:
                print('_',end=' ')
        i=i-1
        print()
        print(pics[m])
        print('Life:'+str(i))
        print('Imagine losing a life')
        m=m+int(6/int(len(randomWord)/2))

        
#ending part of the game is checked here
    if str(i)=='0' :
        print('You lost! You loser haha')
        print('Correct word:'+randomWord)
        exit()
    elif len(allLetters)==len(correctLetters):
        print()
        print('Congratulations You Won!')
        exit()
