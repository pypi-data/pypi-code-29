#!/usr/bin/env python

# Copyright (c) 2006 Bermi Ferrer Martinez
#
# bermi a-t bermilabs - com
# See the end of this file for the free software, open source license (BSD-style).

import re


class Base(object):
    '''Locale inflectors must inherit from this base class inorder to provide
    the basic Inflector functionality'''

    def cond_plural(self, number_of_records, word):
        '''Returns the plural form of a word if first parameter is greater than 1'''

        if number_of_records != 1:
            return self.pluralize(word)
        else:
            return word

    def titleize(self, word, uppercase=''):
        '''Converts an underscored or CamelCase word into a English sentence.
            The titleize function converts text like "WelcomePage",
            "welcome_page" or  "welcome page" to this "Welcome Page".
            If second parameter is set to 'first' it will only
            capitalize the first character of the title.'''

        if(uppercase == 'first'):
            return self.humanize(self.underscore(word)).capitalize()
        else:
            return self.humanize(self.underscore(word)).title()

    def camelize(self, word):
        ''' Returns given word as CamelCased
        Converts a word like "send_email" to "SendEmail". It
        will remove non alphanumeric character from the word, so
        "who's online" will be converted to "WhoSOnline"'''
        return ''.join(w[0].upper() + w[1:] for w in re.sub('[^A-Z^a-z^0-9^:]+', ' ', word).split(' '))

    def underscore(self, word):
        ''' Converts a word "into_it_s_underscored_version"
        Convert any "CamelCased" or "ordinary Word" into an
        "underscored_word".
        This can be really useful for creating friendly URLs.'''

        return re.sub('[^A-Z^a-z^0-9^\/]+', '_',
                      re.sub('([a-z\d])([A-Z])', '\\1_\\2',
                             re.sub('([A-Z]+)([A-Z][a-z])', '\\1_\\2', re.sub('::', '/', word)))).lower()

    def humanize(self, word, uppercase=''):
        '''Returns a human-readable string from word
        Returns a human-readable string from word, by replacing
        underscores with a space, and by upper-casing the initial
        character by default.
        If you need to uppercase all the words you just have to
        pass 'all' as a second parameter.'''

        if(uppercase == 'first'):
            return re.sub('_id$', '', word).replace('_', ' ').capitalize()
        else:
            return re.sub('_id$', '', word).replace('_', ' ').title()

    def variablize(self, word):
        '''Same as camelize but first char is lowercased
        Converts a word like "send_email" to "sendEmail". It
        will remove non alphanumeric character from the word, so
        "who's online" will be converted to "whoSOnline"'''
        word = self.camelize(word)
        return word[0].lower() + word[1:]

    def tableize(self, class_name):
        ''' Converts a class name to its table name according to rails
        naming conventions. Example. Converts "Person" to "people" '''
        return self.pluralize(self.underscore(class_name))

    def classify(self, table_name):
        '''Converts a table name to its class name according to rails
        naming conventions. Example: Converts "people" to "Person" '''
        return self.camelize(self.singularize(table_name))

    def ordinalize(self, number):
        '''Converts number to its ordinal English form.
        This method converts 13 to 13th, 2 to 2nd ...'''
        tail = 'th'
        if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
            tail = 'th'
        elif number % 10 == 1:
            tail = 'st'
        elif number % 10 == 2:
            tail = 'nd'
        elif number % 10 == 3:
            tail = 'rd'

        return str(number) + tail

    def unaccent(self, text):
        '''Transforms a string to its unaccented version.
        This might be useful for generating "friendly" URLs'''
        find = u'\u00C0\u00C1\u00C2\u00C3\u00C4\u00C5\u00C6\u00C7\u00C8\u00C9\u00CA\u00CB\u00CC\u00CD\u00CE\u00CF\u00D0\u00D1\u00D2\u00D3\u00D4\u00D5\u00D6\u00D8\u00D9\u00DA\u00DB\u00DC\u00DD\u00DE\u00DF\u00E0\u00E1\u00E2\u00E3\u00E4\u00E5\u00E6\u00E7\u00E8\u00E9\u00EA\u00EB\u00EC\u00ED\u00EE\u00EF\u00F0\u00F1\u00F2\u00F3\u00F4\u00F5\u00F6\u00F8\u00F9\u00FA\u00FB\u00FC\u00FD\u00FE\u00FF'
        replace = u'AAAAAAACEEEEIIIIDNOOOOOOUUUUYTsaaaaaaaceeeeiiiienoooooouuuuyty'
        return self.string_replace(text, find, replace)

    def string_replace(self, word, find, replace):
        '''This function returns a copy of word, translating
        all occurrences of each character in find to the
        corresponding character in replace'''
        for k in range(0, len(find)):
            word = re.sub(find[k], replace[k], word)

        return word

    def urlize(self, text):
        '''Transform a string its unaccented and underscored
        version ready to be inserted in friendly URLs'''
        return re.sub('^_|_$', '', self.underscore(self.unaccent(text)))

    def demodulize(self, module_name):
        return self.humanize(self.underscore(re.sub('^.*::', '', module_name)))

    def modulize(self, module_description):
        return self.camelize(self.singularize(module_description))

    def foreignKey(self, class_name, separate_class_name_and_id_with_underscore=1):
        ''' Returns class_name in underscored form, with "_id" tacked on at the end.
        This is for use in dealing with the database.'''
        if separate_class_name_and_id_with_underscore:
            tail = '_id'
        else:
            tail = 'id'
        return self.underscore(self.demodulize(class_name)) + tail


class English(Base):
    """
    Inflector for pluralize and singularize English nouns.

    This is the default Inflector for the Inflector obj
    """

    def pluralize(self, word):
        '''Pluralizes English nouns.'''

        rules = [
            ['(?i)(quiz)$', '\\1zes'],
            ['^(?i)(ox)$', '\\1en'],
            ['(?i)([m|l])ouse$', '\\1ice'],
            ['(?i)(matr|vert|ind)ix|ex$', '\\1ices'],
            ['(?i)(x|ch|ss|sh)$', '\\1es'],
            ['(?i)([^aeiouy]|qu)ies$', '\\1y'],
            ['(?i)([^aeiouy]|qu)y$', '\\1ies'],
            ['(?i)(hive)$', '\\1s'],
            ['(?i)(?:([^f])fe|([lr])f)$', '\\1\\2ves'],
            ['(?i)sis$', 'ses'],
            ['(?i)([ti])um$', '\\1a'],
            ['(?i)(buffal|tomat)o$', '\\1oes'],
            ['(?i)(bu)s$', '\\1ses'],
            ['(?i)(alias|status)', '\\1es'],
            ['(?i)(octop|vir)us$', '\\1i'],
            ['(?i)(ax|test)is$', '\\1es'],
            ['(?i)s$', 's'],
            ['(?i)$', 's']
        ]

        uncountable_words = ['equipment', 'information', 'rice', 'money', 'species', 'series', 'fish', 'sheep']

        irregular_words = {
            'person': 'people',
            'man': 'men',
            'child': 'children',
            'sex': 'sexes',
            'move': 'moves'
        }

        lower_cased_word = word.lower()

        for uncountable_word in uncountable_words:
            if lower_cased_word[-1 * len(uncountable_word):] == uncountable_word:
                return word

        for irregular in irregular_words.keys():
            match = re.search('(' + irregular + ')$', word, re.IGNORECASE)
            if match:
                return re.sub('(?i)' + irregular + '$', match.expand('\\1')[0] + irregular_words[irregular][1:], word)

        for rule in range(len(rules)):
            match = re.search(rules[rule][0], word, re.IGNORECASE)
            if match:
                groups = match.groups()
                for k in range(0, len(groups)):
                    if groups[k] is None:
                        rules[rule][1] = rules[rule][1].replace('\\' + str(k + 1), '')

                return re.sub(rules[rule][0], rules[rule][1], word)

        return word

    def singularize(self, word):
        '''Singularizes English nouns.'''

        rules = [
            ['(?i)(quiz)zes$', '\\1'],
            ['(?i)(matr)ices$', '\\1ix'],
            ['(?i)(vert|ind)ices$', '\\1ex'],
            ['(?i)^(ox)en', '\\1'],
            ['(?i)(alias|status)es$', '\\1'],
            ['(?i)([octop|vir])i$', '\\1us'],
            ['(?i)(cris|ax|test)es$', '\\1is'],
            ['(?i)(shoe)s$', '\\1'],
            ['(?i)(o)es$', '\\1'],
            ['(?i)(bus)es$', '\\1'],
            ['(?i)([m|l])ice$', '\\1ouse'],
            ['(?i)(x|ch|ss|sh)es$', '\\1'],
            ['(?i)(m)ovies$', '\\1ovie'],
            ['(?i)(s)eries$', '\\1eries'],
            ['(?i)([^aeiouy]|qu)ies$', '\\1y'],
            ['(?i)([lr])ves$', '\\1f'],
            ['(?i)(tive)s$', '\\1'],
            ['(?i)(hive)s$', '\\1'],
            ['(?i)([^f])ves$', '\\1fe'],
            ['(?i)(^analy)ses$', '\\1sis'],
            ['(?i)((a)naly|(b)a|(d)iagno|(p)arenthe|(p)rogno|(s)ynop|(t)he)ses$', '\\1\\2sis'],
            ['(?i)([ti])a$', '\\1um'],
            ['(?i)(n)ews$', '\\1ews'],
            ['(?i)s$', ''],
        ]

        uncountable_words = ['equipment', 'information', 'rice', 'money', 'species', 'series', 'fish', 'sheep', 'sms']

        irregular_words = {
            'people': 'person',
            'men': 'man',
            'children': 'child',
            'sexes': 'sex',
            'moves': 'move'
        }

        lower_cased_word = word.lower()
        for uncountable_word in uncountable_words:
            if lower_cased_word[-1 * len(uncountable_word):] == uncountable_word:
                return word

        for irregular in irregular_words.keys():
            match = re.search('(' + irregular + ')$', word, re.IGNORECASE)
            if match:
                return re.sub('(?i)' + irregular + '$', match.expand('\\1')[0] + irregular_words[irregular][1:], word)

        for rule in range(len(rules)):
            match = re.search(rules[rule][0], word, re.IGNORECASE)
            if match:
                groups = match.groups()
                for k in range(0, len(groups)):
                    if groups[k] is None:
                        rules[rule][1] = rules[rule][1].replace('\\' + str(k + 1), '')

                return re.sub(rules[rule][0], rules[rule][1], word)

        return word


class Inflector(object):
    """
    Inflector for pluralizing and singularizing nouns.

    It provides methods for helping on creating programs
    based on naming conventions like on Ruby on Rails.
    """

    def __init__(self, Inflector=English):
        assert callable(Inflector), "Inflector should be a callable obj"
        self.Inflector = Inflector()

    def pluralize(self, word):
        '''Pluralizes nouns.'''
        return self.Inflector.pluralize(word)

    def singularize(self, word):
        '''Singularizes nouns.'''
        return self.Inflector.singularize(word)

    def cond_plural(self, number_of_records, word):
        '''Returns the plural form of a word if first parameter is greater than 1'''
        return self.Inflector.cond_plural(number_of_records, word)

    def titleize(self, word, uppercase=''):
        '''Converts an underscored or CamelCase word into a sentence.
            The titleize function converts text like "WelcomePage",
            "welcome_page" or  "welcome page" to this "Welcome Page".
            If the "uppercase" parameter is set to 'first' it will only
            capitalize the first character of the title.'''
        return self.Inflector.titleize(word, uppercase)

    def camelize(self, word):
        ''' Returns given word as CamelCased
        Converts a word like "send_email" to "SendEmail". It
        will remove non alphanumeric character from the word, so
        "who's online" will be converted to "WhoSOnline"'''
        return self.Inflector.camelize(word)

    def underscore(self, word):
        ''' Converts a word "into_it_s_underscored_version"
        Convert any "CamelCased" or "ordinary Word" into an
        "underscored_word".
        This can be really useful for creating friendly URLs.'''
        return self.Inflector.underscore(word)

    def humanize(self, word, uppercase=''):
        '''Returns a human-readable string from word
        Returns a human-readable string from word, by replacing
        underscores with a space, and by upper-casing the initial
        character by default.
        If you need to uppercase all the words you just have to
        pass 'all' as a second parameter.'''
        return self.Inflector.humanize(word, uppercase)

    def variablize(self, word):
        '''Same as camelize but first char is lowercased
        Converts a word like "send_email" to "sendEmail". It
        will remove non alphanumeric character from the word, so
        "who's online" will be converted to "whoSOnline"'''
        return self.Inflector.variablize(word)

    def tableize(self, class_name):
        ''' Converts a class name to its table name according to rails
        naming conventions. Example. Converts "Person" to "people" '''
        return self.Inflector.tableize(class_name)

    def classify(self, table_name):
        '''Converts a table name to its class name according to rails
        naming conventions. Example: Converts "people" to "Person" '''
        return self.Inflector.classify(table_name)

    def ordinalize(self, number):
        '''Converts number to its ordinal form.
        This method converts 13 to 13th, 2 to 2nd ...'''
        return self.Inflector.ordinalize(number)

    def unaccent(self, text):
        '''Transforms a string to its unaccented version.
        This might be useful for generating "friendly" URLs'''
        return self.Inflector.unaccent(text)

    def urlize(self, text):
        '''Transform a string to its unaccented and underscored
        version ready to be inserted in friendly URLs'''
        return self.Inflector.urlize(text)

    def demodulize(self, module_name):
        return self.Inflector.demodulize(module_name)

    def modulize(self, module_description):
        return self.Inflector.modulize(module_description)

    def foreignKey(self, class_name, separate_class_name_and_id_with_underscore=1):
        ''' Returns class_name in underscored form, with "_id" tacked on at the end.
        This is for use in dealing with the database.'''
        return self.Inflector.foreignKey(class_name, separate_class_name_and_id_with_underscore)


# Copyright (c) 2006 Bermi Ferrer Martinez
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to deal in this software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of this software, and to permit
# persons to whom this software is furnished to do so, subject to the following
# condition:
#
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THIS SOFTWARE.
