import os, sys, datetime, inspect, time, random, multiprocessing, multiprocessing.pool


class TreeLogger:

    def __init__(self, outputs='default', autoclose=True, **kwargs):

        if outputs == 'default':

            outputs = [TextFileOutput('log', os.getcwd()), SysStdOutput()]

        else:

            assert type(outputs) is list, 'You must pass a list of Output Objects'

        self.outputs = outputs

        self.closed = False

        self.autoclose = autoclose

        self.open_log()

        return super().__init__(**kwargs)

    def log(self, message, **kwargs):

        treemessage = Tag(message, **kwargs).__str__()

        for output in self.outputs:

            if output.format:

                output.log(treemessage)

            else:

                output.log(message)

        return

    def _opentag(self, treemessage):

        for output in self.outputs:

            if output.format:
                output.log(treemessage)

        return

    def _closetag(self, treemessage):

        for output in self.outputs:

            if output.format:
                output.log(treemessage)

        return

    def open_log(self):

        for output in self.outputs:
            output.open_log('<log> \n')

        return

    def close_log(self):

        for output in self.outputs:

            output.close_log('</log>')

            try:

                output.autoclose = False

            except:

                pass

        return


class Tag():
    escapes = ['"', "'", '<', '>', '&']

    def __init__(self, message, tag='msg', **kwargs):

        self.message = str(message)

        self.kwargs = kwargs

        self.tag = tag

    def __str__(self):

        tag = self.tag

        att = self.kwargs.get('attributes')

        attstring = self._convertattributes(att)

        if any(char in self.message for char in self.escapes):
            self.message = 'see comment <!-- %s -->' % self.message

        return '<%s %s>  %s  </%s> \n' % (tag, attstring, self.message, tag)

    def open(self):

        att = self.kwargs.get('attributes')

        attstring = self._convertattributes(att)

        starttag = '<%s %s> \n' % (self.message, attstring)

        return starttag

    def close(self):

        endtag = '</%s> \n' % self.message

        return endtag

    def _convertattributes(self, attributes=dict()):

        attstring = ''

        if attributes:

            for key, value in attributes.items():

                key = str(key)

                value = str(value)

                if any(char in key for char in self.escapes) or any(char in value for char in self.escapes):

                    pass

                else:

                    attstring = attstring + (' %s = "%s" ' % (key, value))

        return attstring


class OutputObject():

    def __init__(self, **kwargs):
        # output objects should always have a self.format attribute

        return super().__init__(**kwargs)

    def log(self, message):
        return

    def open_log(self, message):
        return

    def close_log(self, message):
        return


class TextFileOutput(OutputObject):

    def __init__(self, basefilename, directory, filetype='txt', autoclose=True, **kwargs):

        self.format = True

        self.basefilename = basefilename

        self.directory = directory

        self.filetype = filetype

        self.file = None

        self.filepath = None

        self.autoclose = autoclose

        self._getfile()

        return super().__init__(**kwargs)

    def _getfile(self):

        newfilename = self.basefilename

        i = 0

        while os.path.isfile(self.directory + '\%s.%s' % (newfilename, self.filetype)):
            i += 1

            newfilename = self.basefilename + str(i)

        self.filepath = self.directory + '\%s.%s' % (newfilename, self.filetype)

        self.file = open(self.filepath, "a")

    def log(self, message):

        self.file.write(message)

    def open_log(self, message):

        self.log(message)

        return

    def close_log(self, message):

        self.log(message)

        return

    def __del__(self):

        if self.autoclose:
            self.close_log('</log>')


class SysStdOutput(OutputObject):

    def __init__(self, **kwargs):
        self.format = False

        return super().__init__(**kwargs)

    def log(self, message):
        print(message)


def treewrap(**deckwargs):
    def superwrapper(func):

        def wrapper(*args, **kwargs):

            global tree

            x = Tag(func.__name__, **deckwargs)

            try:

                tree._opentag(x.open())

                result = func(*args, **kwargs)



            except:

                raise

            finally:

                tree._closetag(x.close())

            return result

        return wrapper

    return superwrapper

    return


tree = TreeLogger(outputs = [SysStdOutput()])


if __name__ == '__main__':


   tree = TreeLogger()


   @treewrap()

   def testfunction(input):


       tree.log(input)


       output = input * 2


       return output


   tree.log('basic logging')


   testfunction(5)


   pass

