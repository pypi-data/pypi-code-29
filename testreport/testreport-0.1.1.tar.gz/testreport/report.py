
import os
from sections import *


def create_directory(directory, **kwargs):
    if isinstance(directory, bool):
        testsuite = kwargs.get("testsuite") or ""
        directory = os.path.join(os.getcwd(), testsuite.lower())
    try:
        os.mkdir(directory)
    except OSError as e:
        if e.errno != 17:
            raise e
    return directory
def get_title(sequence):
    title = filter(lambda x: x[0] == TITLE, sequence)
    if len(title) != 1:
        raise Exception("Test case must provide a single title")
    return title[0][1]

def get_entries(sequence):
    return filter(lambda x: x[0] != TITLE, sequence)

def get_filename(title, extension):
    return title.replace(" ", "_").lower() + extension

def report2Md(sequence, directory, **kwargs):
    directory = create_directory(directory, **kwargs)
    title = get_title(sequence)
    entries = get_entries(sequence)
    filename = os.path.join(directory, get_filename(title, ".md"))
    with open(filename, "w") as fp:
        fp.write("# ")
        fp.write(title)
        fp.write("\n")
        for entry in entries:
            if entry[0] == EXPLANATION:
                fp.write(entry[1])
                fp.write("\n")
            elif entry[0] == TIP:
                fp.write(">")
                fp.write(entry[1].replace("\n", "\n>"))
                fp.write("\n")
            elif entry[0] == CODE:
                fp.write("```\n")
                fp.write(entry[1])
                fp.write("\n```\n")
            else:
                raise Exception("Invalid entry!")
    return filename

def report2Csv(sequence, directory, **kwargs):
    separator = kwargs.get("separator") or ";"
    directory = create_directory(directory, **kwargs)
    title = get_title(sequence)
    entries = get_entries(sequence)
    filename = os.path.join(directory, get_filename(title, ".csv"))
    with open(filename, "w") as fp:
        fp.write(title)
        fp.write("\n")
        for entry in entries:
            fp.write(separator.join(list(entry)))
            fp.write("\n")
    return filename

def report2HTML(sequence, directory, **kwargs):
    from yattag import Doc
    directory = create_directory(directory, **kwargs)
    title = get_title(sequence)
    entries = get_entries(sequence)
    filename = os.path.join(directory, get_filename(title, ".html"))
    doc, tag, text = Doc().tagtext()
    with tag("html"):
        with tag("head"):
            with tag("title"):
                text(title.title())
            # doc.stag("script", src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js")
            with tag("style"):
                text("""

h1 {
    color: white;
    text-align: center;
}

div.code {
	font-size: 20px;
	padding: 5x;
	border-left: 4px solid blue;
}

div.tip {
	display:inline;
	font-size: 20px;
	background-color: lightgray;
    border: solid;
    padding: 20px;
    border-radius: 10px;
    -moz-border-radius: 15px;
}

div.explanation {
	font-size: 20px;

}


code {
	font-family: courier;
}
p {
    
    font-size: 20px;
}
""")

        with tag("body"):
            with tag("p"):
                with tag("h3"):
                    text(title.title())
            for entry in entries:
                with tag("p"):
                    if entry[0] == EXPLANATION:
                        with tag("div", **{"class":"explanation"}):
                            text(entry[1])
                    elif entry[0] == TIP:
                        doc.stag("br")
                        with tag("div", **{"class":"tip"}):
                            text(entry[1])
                        doc.stag("br")
                    elif entry[0] == CODE:
                        doc.stag("br")
                        with tag("div", **{"class":"code"}):
                            with tag("code"):
                                for t in entry[1].split("\n"):
                                    text(t)
                                    doc.stag("br")
                        doc.stag("br")
                    else:
                        raise Exception("Invalid entry!")

    value = doc.getvalue()
    try:
        from BeautifulSoup import BeautifulSoup as bs
        soup=bs(value)
        value = soup.prettify()
    except ImportError:
        pass # if beautifulsoup is not installed, we can use the file without the formating
    with open(filename,"w") as fp:
        fp.write(value)
    return filename


def report2tex(sequence, directory, **kwargs):
    language = kwargs.get("language") or "C"
    directory = create_directory(directory, **kwargs)
    title = get_title(sequence)
    entries = get_entries(sequence)
    tex_start = """\documentclass[a4paper]{article}

\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[colorinlistoftodos]{todonotes}
\usepackage{minted}

\usepackage{tcolorbox}% http://ctan.org/pkg/tcolorbox
% https://tex.stackexchange.com/questions/66154/how-to-construct-a-coloured-box-with-rounded-corners
\definecolor{mycolor}{rgb}{0.698, 0.335, 0.398}% Rule colour


\\newcommand{\mybox}[1]{%
  \setbox0=\hbox{#1}%
  \\begin{tcolorbox}[colframe=mycolor,boxrule=0.5pt,arc=4pt,
        left=6pt,right=6pt,top=6pt,bottom=6pt,boxsep=0pt,width=300pt]
    #1
  \end{tcolorbox}
  }

\\title{TITLE}

\\begin{document}
\maketitle

""".replace("TITLE", title.title())
    filename = os.path.join(directory, get_filename(title, ".tex"))
    tex_end = "\end{document}"
    with open(filename, "w") as fp:
        fp.write(tex_start)
        fp.write("\n")
        for entry in entries:
            if entry[0] == EXPLANATION:
                fp.write(entry[1])
                fp.write("\n\n")
            elif entry[0] == TIP:
                fp.write("\mybox{" + entry[1] + "}")
                fp.write("\n\n")
            elif entry[0] == CODE:
                fp.write("\\begin{minted}{" + language + "}\n" + entry[1] + "\n\end{minted}\n" )
                fp.write("\n```\n")
            else:
                raise Exception("Invalid entry!")
        fp.write(tex_end)
        fp.write("\n")
    return filename


def report2PDF(sequence, directory, **kwargs):
    try:
        from commands import getstatusoutput
    except ImportError: # Python 3
        from subprocess import getstatusoutput
    texfile = report2tex(sequence, directory, **kwargs)
    directory = create_directory(directory, **kwargs)
    title = get_title(sequence)
    filename = os.path.join(directory, get_filename(title, ".pdf"))
    if not os.path.exists(getstatusoutput("which pdflatex")[1]):
        raise Exception("Please ensure pdflatex is installed")
    sts, ret = getstatusoutput("cd {1} && pdflatex  -shell-escape  -halt-on-error {0}" .format(
        texfile, directory))
    if sts !=0:
        raise Exception("Latex error: {0}".format(ret))
    return filename




if __name__ == '__main__':
    s = [
        (TITLE, "title"),
        (EXPLANATION, "explanation"),
        (CODE, """<html>
        <title> </title>
        <body> </body>
        </html>"""),
        (TIP, "a tip"),
        (TIP, """a bigger
        and multine 
        tip""")

    ]
    import tempfile
    tmp = tempfile.mkdtemp()
    print tmp
    # report2Md(s, tmp, testcase="md")
    # report2Csv(s, tmp, testcase="md")
    report2HTML(s, tmp, testcase="md")
    from commands import getoutput as cmd
    print cmd("ls " + tmp)
    print " #### "
    print cmd("google-chrome " + tmp + "/*")
    print cmd("cat " + tmp + "/*")