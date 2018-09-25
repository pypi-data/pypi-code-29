import configparser

class ConfigurationParser:
    parser = configparser.ConfigParser()

    def __init__(self, path):

        self.parser.read(path)
        self.secret_twitter_api_info = self.confParser("twitter_secrete_api_keys")
        self.secret_googleplus_api_info=self.confParser("googleplus_secrete_api_keys")


    def confParser(self, section):

        if not self.parser.has_section(section):
            print("No section information are available in config file for", section)
            return
        # Build dict
        tmp_dict = {}
        for option, value in self.parser.items(section):
            option = str(option)
            value = value.encode("utf-8")
            tmp_dict[option] = value
        return tmp_dict

    def get(self, src):

        if src == "googlePlus_credentials":
            return self.secret_googleplus_api_info
        elif src == "twitter_credentials":
            return self.secret_twitter_api_info