# anoying quiz 1
import random, time, string, collections
questions = 0
score = 0

def intro():#define the intro
    '''introduction'''
    print('welcome to the impossible quiz!')

def play():
    '''play'''
    play = str(input('would you like to play?\n(yes / no)\n'))#take user input to check if they want to play again.
    if play == 'yes' or play == 'y': #user inputs yes
        quiz2()
    else:  #player reutrns no
        print('Dont take '+ play + ' as an answer... play quiz!!!')
        play2()
def play2():
    play()
def quiz(): #part 1 of the quiz
    '''quiz'''
    global questions, score
    userinput = input().upper()
    answer = 'HELLO'
    
    if userinput == answer:
        print('correct')
        questions = questions + 1 #add question number 
        score = int(score)
        score=score + 1
        score = str(score)#convert to string to read

    elif userinput != answer:
        questions = questions + 1
        print('wrong, answer was: '+answer+' duh!!')



def quiz2(): #part 2 of the quiz
    '''quiz2'''
    global questions, score
    while questions <= 9: #check if questions are below 10
        quiz() #play the question

    score = str(score)
    print('your score was '+score+'/10\n ')

    name = input(str('your name: '))
   
    scores =open('lol.txt','a')
    scores.write(''+ name +':'+ score +'\n')
    scores.close()


    start()

def scores1():
    print('\nPeople who have taken quiz:\n')
    with open('lol.txt', 'r') as r:
        for line in sorted(r): # sort linies 
            print(line, end='') # end the list of names

def stats():
    print('\nHigh scores\n')
    with open("lol.txt") as f:

        d = {}

        for line in f:
            column = line.split(":") # split when read an ':'
            names = column[0]  #assgin to colum
            scores = int(column[1].strip())

            count = 0
            while count < 3:
                d.setdefault(names, []).append(scores)
                count = count + 1

        averages=[]
        for name, v in d.items():
            average = (sum(v[-3:])/len(v[-3:]))
            averages.append((name, average))

        for name, average in sorted(averages, key=lambda a: a[1], reverse=True):
            print(name, average)

def lastT():
    with open("lol.txt", mode="r",encoding="utf-8") as fp:
            count = collections.defaultdict(int)
            rev = reversed(fp.readlines())
            rev_out = []

            for line in rev:
                name, value = line.split(':')
                if count[name] >= 3:
                    continue
                count[name] += 1
                rev_out.append((name, value))

    out = list(reversed(rev_out))
    print (out)

def menu():
    choice=input(str('What would you like? a / p / n / T\n'))
    if  choice == 'p':
        play()
    elif choice == 'a':
        scores1()
    elif choice == 'n':
        stats()
    elif choice == 'T':
        lastT()
        

                 
def start(): # start menu
    '''start'''
    intro()
    menu()



start()

#Made By Luigi, Amended By Sam
