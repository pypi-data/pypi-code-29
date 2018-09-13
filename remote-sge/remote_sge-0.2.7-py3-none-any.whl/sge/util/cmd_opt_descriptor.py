from sge.util.serializers import StringSerializer

class CmdOptionAttr(object):
    """
    Descriptor for properties on the JobTemplate class, to translate DRMAA options
    to properly formatted qsub options.

    A qsub option is internally identified by the option name as it is seen
    on the command line, e.g. "-V".

    Setting the attribute on a JobTemplate will result in the value being encoded
    as needed (e.g. boolean values become yes/no, etc), and then stored in the
    :func:`drmaa.JobTemplate.options` dictionary, using *option_name* as its key.

    """
    def __init__(self, option_name, type_converter=StringSerializer, doc=None, del_value=None):
        """
        Args:
            option_name (str): the name of the qsub_ option, as described
                `on the qsub man page`__.
            type_converter

        .. _qsub: http://gridscheduler.sourceforge.net/htmlman/htmlman1/qsub.html
        __ qsub_
        """
        self.option_name = option_name
        self.converter = type_converter
        self.del_value = del_value
        try:
            if doc:
                self.__doc__ = (doc + 
                                "\n\n" + type_converter.doctext() +
                                "\n\nSetting this attribute to %s will cause it to " % str(del_value) + 
                                "be removed from the command options.")
        except Exception as identifier:
            print(option_name)
            print(doc)
            print(type_converter)
            raise identifier

    def __get__(self, instance, _):
        if not self.option_name in instance.qsub_options:
            return self.del_value

        raw_value = instance.qsub_options[self.option_name]
        if self.converter:
            return self.converter.deserialize(raw_value)
        else:
            return raw_value

    def __set__(self, instance, value):
        print(instance)
        if self.converter:
            value = self.converter.serialize(value)

        if value == self.del_value and self.option_name in instance.qsub_options:
            del instance.qsub_options[self.option_name]
        else:
            instance.qsub_options[self.option_name] = value

    def __delete__(self, instance):
        print("deleted in descriptor object")
        del instance.qsub_options[self.option_name]

