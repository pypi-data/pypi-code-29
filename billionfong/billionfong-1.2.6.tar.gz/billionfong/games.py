import random

class bingo():
    def __init__(self):
        answer = random.randint(2,99)
        lower = 1
        upper = 100
        while (True):
            string = str(lower)+" < ? < "+str(upper)+":\t"
            guess = input(string)
            if (RepresentsInt(guess)):
                guess =  int(float(guess))
                if (guess == answer):
                    print ("Bingo!")
                    return
                elif ((lower < guess) and (guess < answer)):
                    lower = guess
                elif ((upper > guess) and (guess > answer)):
                    upper = guess
            else:
                print ("Please input a valid input.")

class martermind():    
    def __init__(self):
        self.game_rules()
        
        answer = random.randint(1,6)*1000 + random.randint(1,6)*100 + random.randint(1,6)*10 + random.randint(1,6)
        
        for i in range (12):
            flag = True
            guess = 0
            while (flag):
                guess = input("Guess?\t")
                if (RepresentsInt(guess)):
                    guess =  int(float(guess))
                    if (self.check_input(guess)):
                        flag = False
                else:
                    print ("Wrong input")
            guess, answer_2, count = self.check_same(guess, answer)
            if (count == 4):
                print ()
                print ("You Win!!!")
                return
            count = self.check_remain(guess, answer_2, count)
            while (count < 4):
                print (".", end="", flush=True)
                count = count + 1
            print ()
        print ()
        print ("Answer is ",answer)
        print ("You Lose!!!")
               
    def game_rules(self):
        print ("----Game Rules - Mastermind----")
        print ("You are given 12 chances to guess out the correct",
               "combinations of 4 numbers between 1 to 6.")
        print ("Hints will be given after every guesses as follows:")
        print ("O: Correct position and number")
        print ("X: Correct number")
        print (".: Wrong number")
        return
    
    def check_input(self, guess):
        for i in [0, 7, 8, 9]:
            if (guess % 10 == i):
                return False
            if ((guess % 100 - guess % 10)/10 == i):
                return False
            if ((guess % 1000 - guess % 100)/100 == i):
                return False
            if ((guess % 10000 - guess % 1000)/1000 == i):
                return False
        if (guess > 6666):
            return False
        if (guess < 1111):
            return False
        return True
        
    def check_same(self, guess, answer):
        count = 0
        if (guess % 10 == answer % 10):
            print ("O", end="", flush=True)
            answer = answer - answer % 10
            guess = guess - guess % 10
            count = count + 1
        if ((guess % 100 - guess % 10) == (answer % 100 - answer % 10)):
            print ("O", end="", flush=True)
            answer = answer - (answer % 100 - answer % 10)
            guess = guess - (guess % 100 - guess % 10)
            count = count + 1
        if ((guess % 1000 - guess % 100) == (answer % 1000 - answer % 100)):
            print ("O", end="", flush=True)
            answer = answer - (answer % 1000 - answer % 100)
            guess = guess - (guess % 1000 - guess % 100)
            count = count + 1
        if ((guess % 10000 - guess % 1000) == (answer % 10000 - answer % 1000)):
            print ("O", end="", flush=True)
            answer = answer - (answer % 10000 - answer % 1000)
            guess = guess - (guess % 10000 - guess % 1000)
            count = count + 1
        return guess, answer, count
    
    def check_remain(self, guess, answer, count):
        guesses = []
        if (guess % 10!= 0):
            guesses.append(guess % 10)
        if ((guess % 100 - guess % 10)/10 != 0):
            guesses.append((guess % 100 - guess % 10)/10)
        if ((guess % 1000 - guess % 100)/100 != 0):
            guesses.append((guess % 1000 - guess % 100)/100)
        if ((guess % 10000 - guess % 1000)/1000 != 0):
            guesses.append((guess % 10000 - guess % 1000)/1000)
            
        answers = []
        if (answer % 10 != 0):
            answers.append(answer % 10)
        if ((answer % 100 - answer % 10)/10 != 0):
            answers.append((answer % 100 - answer % 10)/10)
        if ((answer % 1000 - answer % 100)/100 != 0):
            answers.append((answer % 1000 - answer % 100)/100)
        if ((answer % 10000 - answer % 1000)/1000 != 0):
            answers.append((answer % 10000 - answer % 1000)/1000)
        
        for i in guesses:
            if i in answers:
                print ("X", end="", flush=True)
                count = count + 1
                answers.remove(i)
        return count
    
def RepresentsInt(s):
    if (s.find(".") > 0):
        return False
    try: 
        int(s)
        return True
    except ValueError:
        return False