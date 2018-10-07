from billionfong import games

class billionfong(): 
    def shout (self):
        pass
    def love (self):
        pass
    def play (self, game = None):
        while (True):
            if (game == "bingo"):
                games.bingo()
            elif (game == "mastermind"):
                games.martermind()
            elif (game == 0):
                return
            else:
                print ("Wrong input.")

class child (billionfong):
    def shout (self):
        print ("Fuck You.")
    def love (self):
        print ("I like stitch and snorlax.")

class itdog(billionfong):
    def shout (self):
        print ("IT IT...")
    def love (self):
        print ("I like playing licking CPU.")
        
class musician(billionfong):
    def shout (self):
        print ("Para Bailar La Bamba~")
    def love (self):
        print ("I like singing loudly~")
        
class narcissist(billionfong):
    def shout (self):
        print ("My products are beautiful!")
    def love (self):
        print ("I like all my 15 products!")