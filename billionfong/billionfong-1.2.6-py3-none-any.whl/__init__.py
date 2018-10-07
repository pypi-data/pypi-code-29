from billionfong import billionfong

def create(personality=None):
    if (personality == 'child'):
        return billionfong.child()
    
    elif (personality == 'itdog'):
        return billionfong.itdog()
    
    elif (personality =='musician'):
        return billionfong.musician()
    
    elif (personality =='narcissist'):
        return billionfong.narcissist()
    
    else:
        personality()
        return

def info():
    personalities = ['child', 'narcissist', 'itdog', 'musician']
    print ("Personalities include: ", end="", flush=True)
    print (personalities)
    games = ['bingo', 'mastermind']
    print ("Games include: ", end="", flush=True)
    print (games)
