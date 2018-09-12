from .generator import Generator


def main():
    generator = Generator()
    generator.handle()
    msg = (
        "***************************************************************\n"
        "ATTENTION! You have created the basic settings\n"
        "for launching in production or create DB params,\n"
        "use 'python manage.py secrecy'!\n"
        "To add secret values, use 'python manage.py secrecy --add' \n"
        "Do not forget to add 'development.py' to .gitignore\n"
        "Happy coding! :)\n"
        "***************************************************************\n"
    )
    print(msg)


if __name__ == '__main__':
    main()