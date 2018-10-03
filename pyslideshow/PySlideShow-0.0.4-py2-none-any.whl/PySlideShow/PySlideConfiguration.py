import jsonschema
import json
import sys
import os

class Configuration:
    configuration = dict()
    schema = dict()

    def __init__(self, fn):
        # load slideshow configuration
        with open(fn) as f:
            self.configuration = json.load(f)

        # load schema of slideshow configuration
        schema_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PySlideConfigurationSchema.json')
        with open(schema_filename) as f:
            self.schema = json.load(f)

        # validate the slideshow configuration
        try:
            jsonschema.validate(self.configuration, self.schema)
        except jsonschema.exceptions.ValidationError as e:
            print "Error: Validation of slideshow configuration '%s' failed." % fn
            print e
            sys.exit(1)

    def get_slide_list(self):
        return self.configuration['SlideList']
