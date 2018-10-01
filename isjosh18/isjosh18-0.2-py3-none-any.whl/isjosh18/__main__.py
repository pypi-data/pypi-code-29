import argparse
import requests


URL = 'https://hasjoshturned18yet.com/api.json'


def main():
    parser = argparse.ArgumentParser(description='Is Josh 18?')
    args = parser.parse_args()

    try:
        res = requests.get(URL).json()
    except requests.ConnectionError as e:
        print('Can\'t connect: %s' % e)
        exit(1)

    yes = res['answer'] == 'yes'

    print('Josh is ' + ('' if yes else 'NOT ') + '18.')
    exit(not yes)


if __name__ == '__main__':
    main()
