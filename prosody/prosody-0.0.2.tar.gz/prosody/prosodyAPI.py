from prosody import globals

import aiohttp
import asyncio
import requests
import wave

def register_user(username, password):
    globals.USERNAME = username
    globals.PASSWORD = password

def get_voice_list():
    response_from_server = requests.get(globals.VOICE_END_POINT)
    return response_from_server.json()

def get_detail_of_voice(signature):
    detail_end_point = globals.VOICE_END_POINT + signature
    response_from_server = requests.get(detailEndPoint)
    return response_from_server.json()

def register_voice_sync(emotion, actor, text):
    voiceInfo = {'emotion': emotion, 'text': text, 'wavfile': ''}
    response_from_server = requests.post(globals.VOICE_END_POINT, data=voiceInfo, auth=(globals.USERNAME, globals.PASSWORD))
    signature = response_from_server.json()['signature'] 
    print("Register {} in ttsapi server".format(signature))
    return signature

def generate_voice_sync(signature):
    generating_end_point = globals.VOICE_END_POINT + signature + '/generate/'
    response_from_server = requests.get(generating_end_point)
    file_name = signature + '.wav'
    wave_file = wave.open(file_name, 'w')
    wave_file.setparams((1, 2, 44100, 0, 'NONE', 'Uncompressed'))
    wave_file.writeframesraw(response_from_server.content)
    wave_file.close()
    print("Generate {}".format(file_name))
    
def generate_voices_sync(emotionX, emotionY, actor, *texts):
    str_emotion = '[' + str(emotionX) + ',' + str(emotionY) + ']'
    
    task_list = [generate_voices_helper(str_emotion, actor, text) for text in texts]
    task_loop = asyncio.get_event_loop()
    task_loop.run_until_complete(asyncio.wait(task_list))
    task_loop.close()

async def generate_voices_sync_helper(emotion, actor, text):
    signature = register_voice(emotion, actor, text)
    generate_voice(signature)

def generate_voices(emotionX, emotionY, actor, *texts):
    str_emotion = '[' + str(emotionX) + ',' + str(emotionY) + ']'
    task_list = [generate_voices_helper(str_emotion, actor, text) for text in texts]
    task_loop = asyncio.get_event_loop()
    task_loop.run_until_complete(asyncio.wait(task_list))
    task_loop.close()
    
async def register_voice_async(emotion, actor, text):
    async with aiohttp.ClientSession() as session:
        try:
            auth = aiohttp.BasicAuth(login=globals.USERNAME, password=globals.PASSWORD)
            voice_info = {'emotion': emotion, 'text': text, 'wavfile': ''}
            async with session.post(globals.VOICE_END_POINT, data=voice_info, auth=auth) as response:
                return await response.json()
        except AttributeError as error:
            print(error)

async def generate_voice_async(signature):
    async with aiohttp.ClientSession() as session:
        generating_end_point = globals.VOICE_END_POINT + signature + '/generate/'
        async with session.get(generating_end_point) as response:
            file_name = signature + '.wav'
            wave_file = wave.open(file_name, 'w')
            wave_file.setparams((1, 2, 44100, 0, 'NONE', 'Uncompressed'))
            wave_file.writeframesraw(await response.read())
            wave_file.close()
            print("Generate {}".format(file_name))

async def generate_voices_helper(emotion, actor, text):
    signature_response = await register_voice_async(emotion, actor, text)
    if signature_response:
        signature = signature_response['signature']
        await generate_voice_async(signature)




