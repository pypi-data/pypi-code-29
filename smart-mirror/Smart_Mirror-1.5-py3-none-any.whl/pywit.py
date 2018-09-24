import json
import sys
from recorder import record_audio, read_audio
from wit import Wit


access_token = "K6ZAK63RQWSYWIQYOWAUVQ7PWVRMD66R"
client = Wit(access_token=access_token)




def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
 
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
 
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
 
    resp = None
    # with open('test.wav', 'rb') as f:
    resp = client.speech(audio, None, {'Content-Type': 'audio/wav'})
    print('Yay, got Wit.ai response: ' + str(resp))
 
    # converting response content to JSON format
    # data = json.loads(str(resp))
 
    # get text from data
    text = resp['_text']
 
    # return the text
    return resp

if __name__ == "__main__":
    text =  RecognizeSpeech('myspeech.wav', 4)
    print("\nYou said: {}".format(text))