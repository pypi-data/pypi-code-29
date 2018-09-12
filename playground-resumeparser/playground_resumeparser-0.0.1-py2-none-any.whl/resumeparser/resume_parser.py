'''
Created on Sep 6, 2018

@author: skondapalli
'''

import nltk, glob, re, traceback
from flask import jsonify
from util.data_converter import convert_file_data_to_text


class ResumeParser(object):
    # Set holding all the supported files to be parsed under the resumes folder
    files = None
    
    def parse(self):
        # List holding the final response with extracted details
        response = []
        
        for f in self.files:
            # List (of dictionaries) that will store all of the values for processing purposes : 
            # text, tokens, lines, sentences, resume_details
            print("Reading File %s" % f)
            
            # Dictionary that stores all the data obtained from parsing
            resume_details = {}
            resume_details['fileName'] = f
            
            # Read the file and convert its content to text
            text, resume_details['extension'] = convert_file_data_to_text(f)
            
            # Parse the text and perform the required NLP techniques
            tokens, lines, sentences = self.tokenize(text)
            
            # Extract the necessary information
            resume_details['EmailIds'] = self.extract_email_ids(text)
            resume_details['PhoneNumbers'] = self.extract_phone_numbers(text)
            # resume_details['Name'], resume_details['Names'] = self.extract_names(lines)
            resume_details['Name'] = self.extract_names(lines)
            resume_details['experience'] = self.extract_experience(lines) 

            response.append(resume_details)
            # print (resume_details)
        
        return jsonify(response)
    
    def __init__(self):
        '''
            Constructor : Load all the supported files and trigger the extraction process.
        '''
        # Module(glob) to match certain patterns
        doc_files = glob.glob("../data/resumes-default/*.doc")
        docx_files = glob.glob("../data/resumes-default/*.docx")
        pdf_files = glob.glob("../data/resumes-default/*.pdf")
        text_files = glob.glob("../data/resumes-default/*.txt")

        self.files = set(doc_files + docx_files + pdf_files + text_files)
        print ("%d files identified" % len(self.files))

    def tokenize(self, text):
        '''
           Tokenize the text.
        '''
        try:
            return self.preprocess(text)
        except Exception as e:
            print traceback.format_exc()
            print e
    
    def preprocess(self, document):
        '''
            Process a document with the necessary POS tagging.
            Returns three lists, one with tokens, one with POS tagged lines, one with POS tagged sentences.
        '''
        try:
            # Get rid of special characters
            try:
                document = document.decode('ascii', 'ignore')
            except:
                document = document.encode('ascii', 'ignore')
            # Newlines are one element of structure in the data
            # Helps limit the context and breaks up the data as is intended in resumes - i.e., into points
            # Splitting on the basis of newlines
            lines = [line.strip() for line in document.split("\n") if len(line) > 0] 
            # Tokenize the individual lines
            lines = [nltk.word_tokenize(line) for line in lines]
            # Tag them
            lines = [nltk.pos_tag(line) for line in lines]
            # Below approach is slightly different because it splits sentences not just on the basis of newlines, but also full stops 
            # - (barring abbreviations etc.)
            # But it fails miserably at predicting names, so currently using it only for tokenization of the whole document
            # Split/Tokenize into sentences (List of strings)
            sentences = nltk.sent_tokenize(document)
            # Split/Tokenize sentences into words (List of lists of strings)
            sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
            tokens = sentences
            # Tag the tokens - list of lists of tuples - each tuple is (<word>, <tag>)
            sentences = [nltk.pos_tag(sentence) for sentence in sentences]
            # Convert tokens from a list of list of strings to a list of strings; basically stitches them together
            temp = []
            for token in tokens:
                temp += token
            tokens = temp
            # tokens - words extracted from the doc, lines - split only based on newlines (may have more than one sentence)
            # sentences - split on the basis of rules of grammar
            return tokens, lines, sentences
        except Exception as e:
            print traceback.format_exc()
            print e 

    def extract_email_ids(self, text): 
        '''
            Extract all the possible email id's.
        '''
        emails = None
        try:
            # re.compile(r'\S*@\S*')
            pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
            # Gets all email addresses as a list
            emails = pattern.findall(text)
        except Exception as e:
            print traceback.format_exc()
            print e

        return emails

    def extract_phone_numbers(self, text):
        '''
            Extract all the possible phone numbers.
        '''
        phone_numbers = None
        try:
            # re.compile(r'([+(]?\d+[)\-]?[ \t\r\f\v]*[(]?\d{2,}[()\-]?[ \t\r\f\v]*\d{2,}[()\-]?[ \t\r\f\v]*\d*[ \t\r\f\v]*\d*[ \t\r\f\v]*)')
            pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
            # Understanding the above regular expression
            # +91 or (91) -> [+(]? \d+ -?
            # Meta characters have to be escaped with \ outside of character classes;
            # hyphen has to be escaped inside the character class if not indicating a range
            # General number formats are 123 456 7890 or 12345 67890 or 1234567890 or 123-456-7890, hence 3 or more digits
            # Amendment to above - some also have (0000) 00 00 00 kind of format
            # \s* is any whitespace character - careful, use [ \t\r\f\v]* instead since newlines are trouble
            match = pattern.findall(text)
            # match = [re.sub(r'\s', '', el) for el in match]
            # Get rid of random white spaces - helps with getting rid of 6 digits or fewer (e.g. pin codes) strings
            # substitute the characters we don't want just for the purpose of checking
            match = [re.sub(r'[,.]', '', el) for el in match if len(re.sub(r'[()\-.,\s+]', '', el)) > 6]
            # Taking care of years, eg. 2001-2004 etc.
            match = [re.sub(r'\D$', '', el).strip() for el in match]
            # $ matches end of string. This takes care of random trailing non-digit characters. \D is non-digit characters
            match = [el for el in match if len(re.sub(r'\D', '', el)) <= 15]
            # Remove number strings that are greater than 15 digits
            try:
                for el in list(match):
                    # Create a copy of the list since you're iterating over it
                    if len(el.split('-')) > 3: continue  # Year format YYYY-MM-DD
                    for x in el.split("-"):
                        try:
                            # Error catching is necessary because of possibility of stray non-number characters
                            # if int(re.sub(r'\D', '', x.strip())) in range(1900, 2100):
                            if x.strip()[-4:].isdigit():
                                if int(x.strip()[-4:]) in range(1900, 2100):
                                    # Don't combine the two if statements to avoid a type conversion error
                                    match.remove(el)
                        except:
                            pass
            except Exception as e:
                print traceback.format_exc()
                print e
                pass
            phone_numbers = match
        except Exception as e:
            print traceback.format_exc()
            print e
            pass

        return phone_numbers

    def extract_names(self, lines):
        '''
           Extract all the possible person names. Consider the first occurrence
        '''
        names = []
        name = None
        try:
            # Try a regex chunk parser
            # grammar = r'NAME: {<NN.*><NN.*>|<NN.*><NN.*><NN.*>}'
            grammar = r'NAME: {<NN.*><NN.*><NN.*>*}'
            # Noun phrase chunk is made out of two or three tags of type NN. (ie NN, NNP etc.) - typical of a name. {2,3} won't work, hence the syntax
            # Note the correction to the rule. Change has been made later.
            chunkParser = nltk.RegexpParser(grammar)
            all_chunked_tokens = []
            for tagged_tokens in lines:
                # Creates a parse tree
                if len(tagged_tokens) == 0: 
                    # Prevent it from printing warnings
                    continue  
                chunked_tokens = chunkParser.parse(tagged_tokens)
                all_chunked_tokens.append(chunked_tokens)
                for subtree in chunked_tokens.subtrees():
                    #  or subtree.label() == 'S' include in if condition if required
                    if subtree.label() == 'NAME':
                        for index, leaf in enumerate(subtree.leaves()):
                            # if leaf[0].lower() in indianNames and 'NN' in leaf[1]:
                            if 'NN' in leaf[1]:
                                # Case insensitive matching, as indianNames have names in lower case
                                # Take only noun-tagged tokens
                                # Surname is not in the name list, hence if match is achieved add all noun-type tokens
                                # Pick up to 3 noun entities
                                hit = " ".join([el[0] for el in subtree.leaves()[index:index + 3]])
                                # Check for the presence of commas, colons, digits - usually markers of non-named entities 
                                if re.compile(r'[\d,:]').search(hit): 
                                    continue
                                names.append(hit)
                                # Need to iterate through rest of the leaves because of possible mis-matches
            # Going for the first name hit
            if len(names) > 0:
                names = [re.sub(r'[^a-zA-Z \-]', '', el).strip() for el in names] 
                name = " ".join([el[0].upper() + el[1:].lower() for el in names[0].split() if len(el) > 0])

        except Exception as e:
            print traceback.format_exc()
            print e         
        
        # return name, names[1:]
        return name
    
    def extract_experience(self, lines):
        experience = 'Not Found'
        try:
            # find the index of the sentence where the experience keyword is found and then analyze that sentence
            for sentence in lines:  
                    # string of words in sentence
                    s = " ".join([words[0].lower() for words in sentence])
                    if re.search('experience', s):
                        tokenized_sentence = nltk.word_tokenize(s)
                        tagged_sentence = nltk.pos_tag(tokenized_sentence)
                        entities = nltk.chunk.ne_chunk(tagged_sentence)
                        for subtree in entities.subtrees():
                            for leaf in subtree.leaves():
                                if leaf[1] == 'CD':
                                    experience = leaf[0]
        except Exception as e:
            print traceback.format_exc()
            print e 
        
        return experience

    
if __name__ == '__main__':
    ResumeParser().parse()
    pass
