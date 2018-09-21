from __future__ import print_function
import sys
import ast
import json
import requests
import base64

try:
    from Matrix_def import *
except ImportError:
    from .Matrix_def import *


class CHARLOTTE_DB:
    def __init__(self, IP_ADDRESS_DB, DATABASE_TOKEN):
        self.IP_ADDRESS_DB = IP_ADDRESS_DB
        self.DATABASE_TOKEN = DATABASE_TOKEN

    def get_image(self, table, search_field, search_string, img_field, new_img_name=None):
        base_json = self.get_object(table, search_field, search_string)
        # Check that the get object call succeeded
        if 'ERROR' in str(base_json):
            # return error message from get request
            return str(base_json)
        # Check if string object contains image meta-data
        if '[#@!$IMAGE!@#$]' not in base_json[img_field]:
            return ('Retrieved object is not an image')
        img_str = base_json[img_field]
        # Check if object contains an image string
        if '[#@!$IMAGE!@#$]#89#!_!#89#' in img_str:
            data = img_str.split('#89#!_!#89#')
            # Retrieve image and assign it the same file name the it was used to be stored in
            if new_img_name is not None:
                img = open(new_img_name, 'wb')
                base_str = str(data[2])
                img.write(str(base_str.decode('base64')))
                return 'SUCCESS getting image ' + new_img_name
            else:
                # assign new file name to retrieved image
                img = open(data[1], 'wb')
                base_str = str(data[2])
                img.write(str(base_str.decode('base64')))
                return 'SUCCESS getting image ' + str(data[2])
        else:
            return 'Object is not an image'

    def add_keyed_image(self, table, img_field, img_file_name, key_field, key_string):
        with open(img_file_name, 'rb') as image_file:
            img_str = base64.b64encode(image_file.read())
            # Add meta-data in object to be added as a string encoded image
            meta_data = '[#@!$IMAGE!@#$]#89#!_!#89#' + str(img_file_name) + '#89#!_!#89#'
        json_data = {img_field: meta_data + img_str}
        return self.add_new_keyed_object(table, key_field, json_data)

    def add_batch_uniqueKey(self, table_name, key_field, arr_json_objects):
        # List that contains elements for batch API call.
        input_arr = []
        try:
            for item in arr_json_objects:
                input_arr.append("add_new_object_to_table_uniqueKey_array")
                input_arr.append(table_name)
                key_str = str(item[key_field])
                del item[key_field]
                keys = item.keys()
                vals = item.values()
                # Designated string format for API call
                parsed = [key_field, key_str] + keys + ['end'] + vals + ['end']
                input_arr += parsed
        # Input type check error handling
        except TypeError:
            input_type = str(type(arr_json_objects))
            if 'list' not in input_type:
                raise Exception("Was expecting a list of dicts but got " + input_type + " instead")
            else:
                for item in arr_json_objects:
                    if 'dict' not in str(type(item)):
                        raise Exception(
                            "Was expecting a list of dicts but got a list with a " + str(type(item)) + " instead")
        # Start setting up API call
        url = self.IP_ADDRESS_DB + "/db/%2Abatch_DB_charlotte_json%2A"

        querystring = {"token": self.DATABASE_TOKEN}

        payload = {'json_data': input_arr}
        response = requests.post(url, data=payload, params=querystring, timeout=45)
        try:
            if response.status_code == 200:
                return str(response.content)
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    def simple_object_add_under10(self, table_name, key_field, key_value, field_1=None, value_1=None, field_2=None,
                                  value_2=None, field_3=None, value_3=None, field_4=None, value_4=None, field_5=None,
                                  value_5=None, field_6=None, value_6=None, field_7=None, value_7=None, field_8=None,
                                  value_8=None, field_9=None, value_9=None, field_10=None, value_10=None):
        params = locals()
        # Parse data
        del params['self']
        del params['table_name']
        del params['key_value']
        del params['key_field']
        fin_json = {}
        for key, value in params.items():
            if params[key] is None:
                del params[key]
                continue
            fin_json[key] = value
        return self.add_new_keyed_object(table_name, key_field, fin_json)

    # In Docs
    def get_table_names(self):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_table_names%2A"
        querystring = {"token": self.DATABASE_TOKEN}
        response = requests.request("GET", url, params=querystring, timeout=45)
        try:
            if response.status_code == 200:
                #ast.literal_eval() can only evaluate a string not a bytes literal
                #server will return a bytes literal so decode the response and turn it into
                #a string 'utf-8'
                return ast.literal_eval(response.content.decode('utf-8'))
            else:
                return response.content
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return response.content

    # In Docs
    def get_table_fields(self, table_name):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_fields%2A"

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name}

        response = requests.request("GET", url, params=querystring, timeout=45)
        try:
            # Check if response went as planned
            if response.status_code != 200:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
            # Parse response content and turn it into a list
            fields = re.sub("[\[\]\"]", "", response.text)
            fields = fields.split(",")
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)
        return fields

    # In Docs
    def get_all_objects_json(self, table_name):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_partial_object_data%2A"
        fields = self.get_table_fields(table_name)
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": fields[0],
                       "search_string": ""}

        response = requests.request("GET", url, params=querystring, timeout=45)
        # Check request status and proceed with data parsing if successful
        if response.status_code == 200:
            try:
                data = json.loads(response.content)
                for index in range(0, len(data)):
                    # list comprehension
                    data[index] = {key: value for item in data[index] for key, value in item.items()}
                return data
            # Returns API response if there're no object in DB or other API err message
            except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
                return response.content
        else:
            return 'ERROR: Request did not success - Status ' + str(response.status_code)

    # In Docs
    def create_table(self, table_name, array_of_fields):
        url = self.IP_ADDRESS_DB + "/db/%2Acreate_table%2A"
        # Check for duplicates
        if len(array_of_fields) != len(set(array_of_fields)):
            raise Exception("Cannot have duplicate table fields")
        # Param check
        if len(array_of_fields) < 1:
            raise Exception('ERROR CANNOT HAVE EMPTY FIELDS')
        if table_name == "":
            return Exception('TABLE NAME CANNOT BE EMPTY STRING')
        # Parse request
        array_of_fields = "\"" + ','.join(array_of_fields) + "\""
        # request object - timesout after 10secs
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "array_of_fields": array_of_fields}
        request = requests.request("GET", url, params=querystring, timeout=45)
        # Check response
        try:
            if request.status_code != 200:
                return 'Request Unsuccessful: ' + str(request.status_code)
            else:
                return request.content
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(request.content)

    # In Docs
    def get_object(self, table_name, search_field, search_string):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_object_data%2A"

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": search_field,
                       "search_string": search_string}

        response = requests.request("GET", url, params=querystring, timeout=60)
        # Check request status
        try:
            if response.status_code == 200:
                # If object exists parse and return it
                data = json.loads(response.content)
                for index in range(0, len(data)):
                    data = {key: value for item in data[index] for key, value in item.items()}
                return data
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

            # POST
            # Creates a new table from a csv file
            # first colum is key fields/values

    def upload_csv(self, table_name, csv_file):
        url = self.IP_ADDRESS_DB + "/%2Acsv_upload%2A"
        querystring = {"token": self.DATABASE_TOKEN, 'table_name': table_name}
        with open(csv_file, 'r') as file:
            # Add csv to post payload
            payload = {'csv_file': file}
            response = requests.post(url, data=payload, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return str(response.content)
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def add_new_keyed_object(self, table_name, key_field, json_data):
        url = self.IP_ADDRESS_DB + "/db/%2Aadd_new_object_uniqueKey_json%2A"
        # Check that user input for json is either json or a dict
        type_check = str(type(json_data))
        if "dict" in type_check:
            key_string = json_data[key_field]
            del json_data[key_field]
            json_data = json.dumps(json_data)
        else:
            raise Exception("Expecting json or dict object but got " + type_check + " instead")

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "key_field": key_field,
                       "key_string": key_string}

        payload = {'json_data': json_data}
        response = requests.post(url, data=payload, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return str(response.content)
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def delete_table(self, table_name):
        url = self.IP_ADDRESS_DB + "/db/%2Adelete_table%2A"
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name}

        if table_name == "" or table_name.isspace():
            raise Exception("Table name cannot be empty")

        response = requests.request("GET", url, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return str(response.content)
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def delete_object(self, table_name, search_field, search_string):
        url = self.IP_ADDRESS_DB + "/db/%2Adelete_object%2A"
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": search_field,
                       "search_string": search_string}
        if search_string == "" or search_string.isspace():
            raise Exception("Cannot have empty search_string")

        response = requests.request("GET", url, params=querystring, timeout=45)
        # Check if request succeeded
        try:
            if response.status_code == 200:
                return str(response.content)
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def add_new_field(self, table_name, field_name):
        url = self.IP_ADDRESS_DB + "/db/%2Aadd_new_field%2A"
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": field_name}
        # Check that an empty field was not passed in
        if field_name == "" or field_name.isspace():
            raise Exception("Cannot have empty field name")

        response = requests.request("GET", url, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def rename_table(self, table_name, new_name):
        # API call url
        url = self.IP_ADDRESS_DB + "/db/%2Arename_table%2A"
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "new_table_name": new_name}

        if new_name == "" or new_name.isspace():
            raise Exception("New table name cannot be empty")

        response = requests.request("GET", url, params=querystring, timeout=45)
        # Check if request succeeded
        try:
            if response.status_code == 200:
                if "SUCCESS" in response.content:
                    # Format name change
                    return "SUCCESS " + table_name + " changed to " + new_name
                else:
                    return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def update_field_name(self, table_name, field_name, new_name):
        url = self.IP_ADDRESS_DB + "/db/%2Aupdate_fieldname%2A"
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": field_name,
                       "new_field_name": new_name}
        # Check that an empty name was not passed in
        if new_name == "" or new_name.isspace():
            raise Exception("New field name cannot be empty")

        response = requests.request("GET", url, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                if "SUCCESS" in response.content:
                    return "SUCCESS " + field_name + " changed to " + new_name
                else:
                    return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def search_partial_matches(self, table_name, field_name, search_string):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_partial_object_data%2A"
        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": field_name,
                       "search_string": search_string}
        # Check that empty field name was not passed in
        if field_name == "" or field_name.isspace():
            raise Exception("Cannot have empty field name")

        response = requests.request("GET", url, params=querystring, timeout=45)
        # Check if request succeeded
        try:
            if response.status_code == 200:
                return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def reinit(self):
        url = self.IP_ADDRESS_DB + "/db/%2Ainitialize%2A"
        querystring = {"token": self.DATABASE_TOKEN}
        response = requests.request("GET", url, params=querystring, timeout=45)
        # Return server status as a string
        return response.content

    # In Docs
    def update_object(self, table_name, key_field, key_string, json_data):
        url = self.IP_ADDRESS_DB + "/db/%2Aupdate_DB_charlotte_json%2A"
        # Make sure that a json formatted string was passed or a dict
        type_check = str(type(json_data))
        if not "str" in type_check:
            if "dict" in type_check:
                json_data = json.dumps(json_data)
            # Give an error if no possible json object was passed
            else:
                raise Exception("Expecting json or dict object but got [" + type_check + "] instead")

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": key_field,
                       "search_string": key_string}
        payload = {'json_data': json_data}
        response = requests.post(url, data=payload, params=querystring, timeout=45)
        # Check if request succeeded
        try:
            if response.status_code == 200:
                return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def add_object_noKey(self, table_name, key_field, key_string, json_data):
        url = self.IP_ADDRESS_DB + "/db/%2Aadd_new_object_NOuniqueKey_json%2A"
        # Check that a json object was passed in (if string is not json formatted, server will let user know)
        type_check = str(type(json_data))
        if not "str" in type_check:
            if "dict" in type_check:
                json_data = json.dumps(json_data)
            else:
                raise Exception("Expecting json or dict object but got [" + type_check + "] instead")

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "key_field": key_field,
                       "key_string": key_string}

        payload = {'json_data': json_data}
        # Send db request with a 45 second timeout
        response = requests.post(url, data=payload, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def add_matrix(self, table_name, key_field, key_string, matrix_field, matrix):
        url = self.IP_ADDRESS_DB + "/db/%2Aadd_new_object_uniqueKey_json%2A"
        # Make sure that a numpy array was passed in
        type_check = str(type(matrix))
        if "numpy.ndarray" in type_check:
            matrix = np_matrix_to_str(matrix)
        # if a list was passed in instead. Convert it to a numpy array
        elif "list" in type_check:
            matrix = py_matrix_to_str(matrix)
        else:
            raise Exception(
                "Was expecting either a numpy matrix, list matrix, or a tensor but got " + type_check + " instead")

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "key_field": key_field,
                       "key_string": key_string}

        json_data = json.dumps({matrix_field: matrix})
        payload = {"json_data": json_data}
        # Send request
        response = requests.post(url, data=payload, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return response.content
            else:
                return 'ERROR: Request did not succeed - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def add_tensor(self, table_name, key_field, key_string, tensor_field, tensor):
        url = self.IP_ADDRESS_DB + "/db/%2Aadd_new_object_uniqueKey_json%2A"

        type_check = str(type(tensor))
        # Check that a tensor was passed in
        if "tensorflow" not in type_check:
            raise Exception("Was a expecting a tensor but got a " + type_check + " instead")

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "key_field": key_field,
                       "key_string": key_string}

        tensor = tensor_to_str(tensor)
        json_data = json.dumps({tensor_field: tensor})
        payload = {"json_data": json_data}

        response = requests.post(url, data=payload, params=querystring, timeout=45)
        try:
            # Check if request succeeded
            if response.status_code == 200:
                return response.content
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    #Not in docs
    def run_script(self, script_file_name):
        url = self.IP_ADDRESS_DB + "/db/%2Arun_script%2A"
        querystring = {"token": self.DATABASE_TOKEN}
        #Read in script file to be run on server
        with open(script_file_name, 'r') as fin:
            script_file = fin.read()
            if 'main_function' not in script_file:
                raise Exception('Script file needs to contains a method called \'main_function\' for the script to properly run in Charlotte_DB')
            payload = {'script': script_file }
            response = requests.post(url, data = payload, params = querystring, timeout = 45)
        try:
            if response.status_code == 200:
                return response.content.decode('utf-8')
            else:
                return 'ERROR: Request did not success - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, KeyError, ValueError, OSError, Exception):
            return str(response.content)

    # In Docs
    def get_matrix(self, table_name, search_field, search_string, matrix_field):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_object_data%2A"

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": search_field,
                       "search_string": search_string}

        response = requests.request("GET", url, params=querystring, timeout=45)
        if response.status_code == 200:
            # Check for matrix meta-data to determine was kind of matrix was passed in
            try:
                if sys.version_info[0] < 3:
                    data = json.loads(response.content)
                else:
                    data = response.content
                    data = json.loads(data.decode('utf-8'))
                data = data[0]
                data = {key: value for item in data for key, value in item.items()}
                matrix_str = data[matrix_field]
                if matrix_str[:6] == "PYTHON":
                    matrix_str = matrix_str.encode('ascii', 'ignore')
                    data = str_to_py_matrix(matrix_str)
                    return data
                elif matrix_str[:5] == "NUMPY":
                    matrix_str = matrix_str.encode('ascii', 'ignore')
                    data = str_to_np_matrix(matrix_str)
                    return data
                else:
                    raise Exception("Called object is not a matrix")
            except KeyError:
                raise Exception("Matrix field DNE")
            except (RuntimeError, TypeError, NameError, ValueError, OSError, Exception):
                return response.content
        else:
            return 'ERROR: Request did not succeed - Status ' + str(response.status_code)

    # In Docs
    def get_tensor(self, table_name, search_field, search_string, tensor_field):
        url = self.IP_ADDRESS_DB + "/db/%2Aget_object_data%2A"

        querystring = {"token": self.DATABASE_TOKEN, "table_name": table_name, "field_name": search_field,
                       "search_string": search_string}

        response = requests.request("GET", url, params=querystring, timeout=45)
        if response.status_code == 200:
            try:
                if sys.version_info[0] < 3:
                    data = json.loads(response.content)
                else:
                    data = response.content
                    data = json.loads(data.decode('utf-8'))
                data = data[0]
                data = {key: value for item in data for key, value in item.items()}
                tensor_str = data[tensor_field]
                if "tensor" in tensor_str:
                    tensor = tensor_str.encode('ascii', 'ignore')
                    tensor = str_to_tensor(tensor)
                    return tensor
                else:
                    raise Exception("Called object is not a tensor")
            except KeyError:
                raise Exception("Tensor field DNE")
            except (RuntimeError, TypeError, NameError, ValueError, OSError, Exception):
                return response.content
        else:
            return 'ERROR: Request did not succeed - Status ' + str(response.status_code)

    # In Docs
    def get_object_count(self, table_name):
        data = self.get_all_objects_json(table_name)
        return len(data)

    # In Docs
    def get_status(self):
        url = self.IP_ADDRESS_DB + "/db/%2Astatus%2A"
        querystring = {"token": self.DATABASE_TOKEN}

        response = requests.request("GET", url, params=querystring, timeout=45)
        try:
            # Check request status
            if response.status_code == 200:
                # return response as a string
                return response.content
            else:
                return 'ERROR: Request did not succeed - Status ' + str(response.status_code)
        except (RuntimeError, TypeError, NameError, ValueError, OSError, Exception):
            return response.content
