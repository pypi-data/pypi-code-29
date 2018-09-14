import requests
import json
from urllib.parse import unquote

class VeriUsAPIGateway:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __text_cleaner(self, text):
        return unquote(text).replace('\r\n',' ').replace('"'," ").replace('\t',' ').replace('\n', ' ').replace('\'', ' ')

    def __text_cleaner_pos(self, text):
        return unquote(text).replace('\r\n',' ').replace('"'," ").replace('\t',' ').replace('\n', ' ').replace('\'', '')

    def __json_response(self, port, url, data):
        headers = {'Content-Type': 'application/json',}
        response = requests.post('http://167.99.142.246:' + port + '/' + url, headers=headers,
                             data=data.encode('utf-8'), auth=(self.username, self.password))
        return json.loads(response.text)

    def __postToWebService(self, port, url, text1, text2 = None, key="data"):
        if not text2:
            text = self.__text_cleaner(text1)
            data = '{"text":"' + text + '"}'
            return self.__json_response(str(port), url, data)[key]
        else:
            text1 = self.__text_cleaner(text1)
            text2 = self.__text_cleaner(text2)

            data = '{"text1":"' + text1 + '","text2":"' + text2 + '"}'
            return self.__json_response(str(port), url, data)[key]


    def getTextSimilarity(self, text1, text2):
        return self.__postToWebService(8001, "text_sim", text1, text2, "similarity_tf")

    def getSemanticSimilarity(self, text1, text2):
        return self.__postToWebService(8002, "semantic_sim", text1, text2, "similarity")


    def getLanguage(self, text):
        return self.__postToWebService(8003, "langdetect", text)

    def getPartofSpeechTags(self, text):
        text = self.__text_cleaner(text)

        data = '{"text":"'+text+'"}'
        json_data = self.__json_response("8004", "pos-tag", data)
        try:
            word_list = json_data["word_list"]
            tag_list = json_data['prediction_list']
        except:
            return json_data

        tag_list = tag_list.replace("[", "").replace("]", "").replace(" ", "").split(",")
        for index, item in enumerate(tag_list):
            if item is "0":
                tag_list[index] = "Noun"
            if item is "1":
                tag_list[index] = "Number"
            if item is "2":
                tag_list[index] = "Adjective"
            if item is "3":
                tag_list[index] = "Verb"
            if item is "4":
                tag_list[index] = "Postp"
            if item is "5":
                tag_list[index] = "Punctuation"
            if item is "6":
                tag_list[index] = "Determiner"
            if item is "7":
                tag_list[index] = "Conjunction"
            if item is "8":
                tag_list[index] = "Adverb"
            if item is "9":
                tag_list[index] = "Pronoun"
            if item is "10":
                tag_list[index] = "Question"
            if item is "11":
                tag_list[index] = "Interjection"
            if item is "12":
                tag_list[index] = "Negp"

        return dict(zip(word_list, tag_list))

    def getAbusive(self, text):
        return self.__postToWebService(8005, "abusive-content-detection", text)

    def getSummary(self, text):
        return self.__postToWebService(8006, "turkish-text-summarizer", text)

    def getKeywords(self, text):
        return self.__postToWebService(8007, "keyword-extractor", text)

    def getNamedEntities(self, text):
        text = self.__text_cleaner(text)

        data = '{"text":"'+text+'"}'
        json_data = self.__json_response("8008", "named-entity-recognition", data)
        try:
            word_list = json_data["word_list"]
            tag_list = json_data['prediction_list']
        except:
            return json_data

        tag_list = tag_list.replace("[", "").replace("]", "").replace(" ", "").split(",")
        for index, item in enumerate(tag_list):
            if item is "0":
                tag_list[index] = "Organization"
            if item is "1":
                tag_list[index] = "Other"
            if item is "2":
                tag_list[index] = "Date"
            if item is "3":
                tag_list[index] = "Occupation"
            if item is "4":
                tag_list[index] = "Person"
            if item is "5":
                tag_list[index] = "Location"
            if item is "6":
                tag_list[index] = "Misc"

        return dict(zip(word_list, tag_list))

    def getDistorted(self, text):
        return self.__postToWebService(8009, "distorted-language-detection", text)

    def getIntent(self, text):
        return self.__postToWebService(8011, "intent-detection", text)

    def getShortNewsClass(self, text):
        return self.__postToWebService(8012, "short-news-classification", text)

    def getTaxonomy(self, text):
        return self.__postToWebService(8013, "taxonomy_web", text, key="result")

    def getNewsClass(self, text):
        return self.__postToWebService(8014, "news-classification", text)

    def getSemanticSimilarityECommerce(self, text1, text2):
        return self.__postToWebService(8015, "semantic_sim_ecommerce", text1=text1, text2=text2, key="similarity")

    def getNormal(self, text):
        return self.__postToWebService(8016, "normalization", text)

    def getDeasciified(self, text):
        return self.__postToWebService(8017, "deasciifier", text)

    def getProductCategory(self, text):
        return self.__postToWebService(8018, "product-classification", text, key="result")

    def getMorphology(self, text):
        text = self.__text_cleaner(text)
        data = '{"data":"' + text + '"}'
        return self.__json_response(str(8019), "morphology", data)['data']
