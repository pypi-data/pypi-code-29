'''
Created on Sep 6, 2018

@author: skondapalli
'''

from cStringIO import StringIO
import subprocess

# from docx import Document
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from docx2txt import docx2txt
import traceback

    
def convert_file_data_to_text(filePath):
    '''
        Converts the file content to text based on the file type. 
        Used docx2text to include header, footer and hyper links as part of data conversion
    '''
    
    text = None
    extension = filePath.split(".")[-1].lower()
    try:
        if extension == "txt":
            f = open(filePath, 'r')
            text = f.read()
            f.close() 
        elif extension == "doc":
            # Run a shell command and store the output as a string
            # Antiword is used for extracting data out of Word docs. Does not work with docx, pdf etc.
            text = subprocess.Popen(['antiword', filePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        elif extension == "docx":
            # document = Document(filePath)
            # Read the headers as XML content and parse it accordingly to extract the text
            # headers = [x.blob.decode() for x in document.part.package.parts if x.partname.find('header')>0]
            text = docx2txt.process(filePath)
            # text = "\n".join([convert_docx_paragraph_to_text(paragraph) for paragraph in document.paragraphs])
        elif extension == "pdf":
            # May have a potential formatting loss for unicode characters
            resourceManager = PDFResourceManager()
            stringIO = StringIO()
            laparams = LAParams()
            textConverter = TextConverter(resourceManager, stringIO, 'utf-8', laparams=laparams)
            f = file(filePath, 'rb')
            interpreter = PDFPageInterpreter(resourceManager, textConverter)
            for page in PDFPage.get_pages(f, set(), 0, "", True, check_extractable=True):
                interpreter.process_page(page)
            f.close()
            textConverter.close()
            text = stringIO.getvalue()
            stringIO.close()
        else:
            print 'Unsupported format : ' + extension
            text = ''
        return text, extension
    except Exception as e:
        print traceback.format_exc()
        print e
        return '', ''
        pass


def convert_docx_paragraph_to_text(p):
    '''
        Used to include hyper links as part of data conversion using python docx module
    '''
    
    rs = p._element.xpath('.//w:t')
    return u" ".join([r.text for r in rs])
