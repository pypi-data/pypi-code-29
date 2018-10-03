__all__,stdouthook,stderrhook=['startstdoutcapture','stdouthook','startstderrcapture','stderrhook'],[],[]
import sys
def startstdoutcapture():
    global sys, stdouthook
    sys.stdout.writeo=sys.stdout.write
    def write(text):
        global stdouthook
        stdouthook.append(text)
        sys.stdout.writeo(text)
    sys.stdout.write=write
def startstderrcapture():
    global sys, stderrhook
    sys.stderr.writeo=sys.stderr.write
    def write(text):
        global stderrhook
        stderrhook.append(text)
        sys.stderr.writeo(text)
    sys.stderr.write=write
