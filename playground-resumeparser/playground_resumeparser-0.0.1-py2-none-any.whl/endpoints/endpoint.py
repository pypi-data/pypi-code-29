'''
Created on Sep 6, 2018

@author: skondapalli
'''

from flask import Flask
from resumeparser import resume_parser

app = Flask(__name__)


@app.route("/parse-resumes", methods=['GET', 'POST'])
def parse_resumes():
    return resume_parser.ResumeParser().parse();


@app.route("/parse-resume", methods=['GET', 'POST'])
def parse_resume():
    return resume_parser.ResumeParser().parse();


@app.route("/health-check", methods=['GET'])
def health_check():
    return resume_parser.ResumeParser().parse();


@app.route("/", methods=['GET', 'POST'])
def welcome():
    return "Welcome to Playground Resume Parser";


if __name__ == '__main__':
    app.run(debug=True)
