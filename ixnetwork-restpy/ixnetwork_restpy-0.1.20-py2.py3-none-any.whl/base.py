from inspect import isclass
from ixnetwork_restpy.connection import Connection
from ixnetwork_restpy.errors import NotFoundError
from ixnetwork_restpy.files import Files


try:
    basestring
except NameError:
    basestring = str


class Base(object):
    """Base
    
    Designed around __iter__, __next__, __getitem__
    _object_properties is a list of property dicts returned by the server
    _index is the current pointer into the _object_properties
    _properties returns the current properties as dictated by _index
    """
    def __init__(self, parent):
        self._parent = parent
        if self._parent is not None:
            self._connection = parent._connection
        self._set_properties(None, clear=True)

    def __iter__(self):
        self._index = -1
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self._index + 1 >= len(self._object_properties):
            raise StopIteration
        else:
            self._index += 1
        return self

    def __getitem__(self, index):
        if index >= len(self._object_properties):
            raise IndexError		
        else:
            self._index = index
        return self

    @property
    def parent(self):
        """The parent object of this object
        
        Returns:
            obj(Base): The parent object of this object

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._parent

    @property
    def index(self):
        """The current index to the internal property array

        Returns:
            number:
        """
        return self._index

    def __len__(self):
        """The total number of objects encapsulated by this object

        Returns: 
            number: 
        """
        return len(self._object_properties)

    @property
    def href(self):
        """The hypertext reference of the current object
        
        Returns: 
            str: The fully qualified hypertext reference of the current object

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_attribute('href')

    @property
    def _properties(self):
        return self._object_properties[self._index]

    def _clear(self):
        self._object_properties = []
        self._index = len(self._object_properties) - 1

    def _check_arg_type(self, object_to_test, arg_type):
        if isinstance(object_to_test, arg_type) is not True:
            raise TypeError('the parameter supplied is of %s but must be of <type \'%s\'>' % (type(object_to_test), arg_type.__name__))

    def _get_attribute(self, name):
        """The main accessor for all attributes
        """
        try:
            return self._properties[name]
        except Exception as e:
            raise NotFoundError('The attribute %s is not in the internal list of object dicts. (%s)' % (name, e.message))
  
    def _set_attribute(self, name, value):
        """Update a property on the server and save it locally if there is no exception
        """
        try:
            self._update({name: value})
            self._properties[name] = value
        except Exception as e:
            raise e
        
    def _dump(self):
        """Returns a dump of the current instance
        """
        if len(self) == 0:
            dump = '%s:' % (self.__class__.__name__)
        else:
            dump = '%s[%s]: %s' % (self.__class__.__name__, self._index, self.href)
            methods = dir(self)
            for key in sorted(self._properties.keys()):
                if key in ['href']:
                    continue
                property_name = '%s%s' % (key[0].upper(), key[1:])
                if property_name in methods:
                    dump += '\n\t%s: %s' % (property_name, self._properties[key])
        return dump

    def __str__(self):
        return self._dump()

    def __repr__(self):
        return self._dump()

    def _build_payload(self, locals_dict, method_name=None):
        """Build and return a payload dictionary

        Ignore the following:
            key of self
            any key not in the internal dictionary
            value of None or Multivalue
        
        Returns: 
            dict: if there are items in the payload after processing of the locals_dict is complete
            None: if there are no items in the payload
        """
        from ixnetwork_restpy.multivalue import Multivalue
        payload = {}
        if locals_dict is not None:
            for key, value in locals_dict.items():
                if key == 'self' or value is None or isinstance(value, Multivalue):
                    continue
                if isclass(value) is True:
                    continue
                if method_name is not None:
                    attribute_name = key
                else:
                    attribute_name = '%s%s' % (key[0].lower(), key[1:])
                payload_value = self._build_value(key, value, method_name=method_name)
                if payload_value is not None:
                    payload[attribute_name] = payload_value
        if bool(payload) is True:
            return payload
        else:
            return None

    def _build_value(self, key, value, method_name=None):
        if isinstance(value, Files):
            if value.is_local_file:
                upload_url = '%s/files?filename=%s' % (self.href[0:self.href.find('ixnetwork') + len('ixnetwork')], value.file_name)
                self._connection._execute(upload_url, payload=value)
            return value.file_name
        elif isinstance(value, Base):
            is_list = False
            if method_name is not None:
                method_param = getattr(self.__class__, method_name).__doc__.replace('\n', '').replace('\t', '').replace(' ', '')
                is_list = method_param.find('%s(list(' % key) != -1
            elif hasattr(self.__class__, key) is True:
                returns = getattr(self.__class__, key).__doc__.replace('\n', '').replace('\t', '').replace(' ', '')
                is_list = returns.find('Returns:list(') != -1
            if is_list is True:
                hrefs = []
                for list_value in value:
                    hrefs.append(list_value.href)
                return hrefs
            else:
                return value.href
        elif isinstance(value, list):
            list_values = []
            for list_item in value:
                list_value = self._build_value(key, list_item)
                if list_value is not None:
                    list_values.append(list_value)
            return list_values
        else:
            return value

    def _create(self, locals_dict):
        payload = self._build_payload(locals_dict)
        url = '%s/%s' % (self.parent.href, self._SDM_NAME)
        properties = self._connection._create(url, payload)
        self._set_properties(properties)
        return self

    def _set_properties(self, properties, clear=False):
        from ixnetwork_restpy.multivalue import Multivalue

        if clear is True:
            self._clear()
        if properties is None:
            return

        # add an empty object dictionary to the internal list of object dictionaries
        self._object_properties.append(dict())
        self._index = len(self._object_properties) - 1

        # populate the current object dictionary
        # replace /multivalue object reference with a Multivalue object
        for key in properties.keys():
            value = properties[key]
            if key != 'href' and value is not None and isinstance(value, basestring) and value.find('/ixnetwork/multivalue') != -1:
                self._properties[key] = Multivalue(self, value)
            elif key == 'links':
                continue
            else:
                self._properties[key] = value
        
        # if href is missing then try backfilling it using either links or id
        if 'href' not in self._properties.keys():
            if 'links' in properties.keys():
                self._properties['href'] = properties['links'][0]['href']
            elif 'id' in properties.keys():
                self._properties['href'] = '%s/%s/%s' % (self.parent.href, self._SDM_NAME, properties['id'])        

    def _update(self, locals_dict):
        payload = self._build_payload(locals_dict)
        if payload is not None:
            self._connection._update(self._properties['href'], payload)
    
    def _delete(self):
        try:
            payload = []
            for properties in self._object_properties:
                payload.append({'id': properties['id']})
            url = '%s/%s' % (self._parent.href, self._SDM_NAME)
            if len(payload) > 0:
                self._connection._delete(url, payload)
                self._clear()
        except Exception as e:
            raise e

    def _execute(self, operation, child=None, payload=None, response_object=None):
        url = self._properties['href']
        if child is not None:
            url = '%s/%s' % (url, child)
        if operation is not None:
            url = '%s/operations/%s' % (url, operation.lower())

        payload = self._build_payload(payload, method_name=operation)
        response = self._connection._execute(url, payload)
        if response_object is None:
            return response

    def refresh(self):
        """Refresh the contents of this object

        Returns: 
            obj: self

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        ids = ''
        for properties in self._object_properties:
            ids = '%s|%s' % (ids, properties['id'])
        return self._select(locals_dict={'id': '(%s)' % ids.strip('|')})

    def _select(self, locals_dict=dict()):
        payload = {
            'selects': [
                {
                    'from': self.parent.href,
                    'properties': [],
                    'children': [
                        {
                            'child': self._SDM_NAME,
                            'properties': ['*'],
                            'filters': []
                        }
                    ],
                    'inlines': []
                }
            ]
        }
        for key in locals_dict.keys():
            if key == 'self' or locals_dict[key] is None or isclass(locals_dict[key]):
                continue
            child_filter = {
                'property': '%s%s' % (key[0].lower(), key[1:]),
                'regex': locals_dict[key]
            }
            payload['selects'][0]['children'][0]['filters'].append(child_filter)
        end = len(self.parent.href)
        if 'ixnetwork' in self.parent.href:
            end = self.parent.href.index('ixnetwork') + len('ixnetwork')
        url = '%s/operations/select' % self.parent.href[0:end]
        response = self._connection._execute(url, payload)
        self._set_properties(None, clear=True)
        if self._SDM_NAME in response[0].keys():
            if isinstance(response[0][self._SDM_NAME], list):
                for item in response[0][self._SDM_NAME]:
                    self._set_properties(item)
            else:
                self._set_properties(response[0][self._SDM_NAME])
        self._index = len(self._object_properties) - 1
        return self
