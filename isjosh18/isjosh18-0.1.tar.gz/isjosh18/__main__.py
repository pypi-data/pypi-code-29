import requests


URL = 'https://hasjoshturned18yet.com/api.json'

def main():
    try:
        res = requests.get(URL).json()
    except requests.ConnectionError as e:
        exit('Can\'t connect: %s' % e)

    yes = res['answer'] == 'yes'

    print('Josh is ' + ('' if yes else 'NOT ') + '18.')
    exit(not yes)

if __name__ == '__main__':
    main()
