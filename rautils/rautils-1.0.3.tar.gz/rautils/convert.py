import os


def html2PDF(location):
    if os.path.isdir(location):
        cwd = os.getcwd()
        os.chdir(location)

        for file in os.listdir(location):
            if file.endswith(".html"):
                file = os.path.join(location,
                                    file).split('.html')[0]
                os.chdir(r'''C:\Program Files\wkhtmltopdf\bin''')
                os.system(f'''.\wkhtmltopdf.exe "{file}.html" "{file}.pdf" ''')

        os.chdir(cwd)
    elif os.path.isfile(location):
        cwd = os.getcwd()
        location = os.path.abspath(location)
        file = location.split('html')[0]

        os.chdir(r'''C:\Program Files\wkhtmltopdf\bin''')
        os.system(f'''.\wkhtmltopdf.exe "{file}.html" "{file}.pdf" ''')

        os.chdir(cwd)
    else:
        raise ValueError(
            'html2PDF: location must be a dir or path')
