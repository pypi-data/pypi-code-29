
from fitchain import constants
import faker as fk
import pandas as pd
import numpy as np
import logging
# import constants
import random
# from random import randint
import string as s
from faker.providers import BaseProvider
from PIL import Image
import os
import sys
import inspect
from pathlib import Path

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print('parent dir=', parentdir)
sys.path.insert(0, parentdir)


# preload image background
bg = Image.open(os.path.join(parentdir + "/static", 'happy_cat.jpg'))
bg_w, bg_h = bg.size


def open(schema, file):
    return _load_dataset(file, schema)


def open_tree(schema, file):
    return DataSetTree(schema, file)


def _generate_image(schema):
    w = int(schema["width"])
    h = int(schema["height"])
    type = schema["type"]
    bands = schema["bands"]
    histogram = schema["histogram"]
    # Take only the Red counts
    l1 = histogram[0:256]
    # Take only the Blue counts
    l2 = histogram[256:512]
    # Take only the Green counts
    l3 = histogram[512:768]
    print('w=', w, "h=", h)
    if set(bands) == {'R', 'G', 'B'}:
        mode = "RGB"
        # who likes random when we have cats :)
        # pixels = np.random.random((w, h, 3))
        # img = Image.fromarray(pixels, mode)
        img = Image.new(mode, (w, h))
        # fill new image of cats :)
        for i in range(0, w, bg_w):
            for j in range(0, h, bg_h):
                img.paste(bg, (i, j))

        return img

    raise ValueError("unsupported color space %s" % bands)


def _generate_csv(schema):
    # For more complex types check https://github.com/joke2k/faker
    fake = fk.Faker()
    fake.add_provider(FitchainDataProvider)
    numrecords = 1000
    logging.info('Generating %s fake records from schema', numrecords)

    if schema['format'] == 'pandas.dataframe':
        data = {}
        # scan each field and generate dummy
        for field in schema['fields']:
            logging.info('Processing field %s', field['name'])
            dummy_content = []
            types = field['type'].keys()
            stats = field['stats']
            lens = stats['length']

            for t in types:
                nelems = field['type'][t]  # elements of this type
                # print('Current type=', t, 'num_elements=', nelems, 'lens=', lens)

                ###############################
                # Fake primitive types
                ###############################
                if t == constants.FITCHAIN_INT:
                    for l in lens:
                        n = int(l)
                        r = lens[l]
                        # print(n,r, type(n), type(r), int(nelems*r))
                        numrecs = int(nelems*r)
                        logging.info('Generating numrecs=%s with n=%s digits', numrecs, n)
                        for i in range(numrecs):
                            dummy_int = fake.integer_with_n_digits(n)
                            dummy_content.append(dummy_int)

                if t == constants.FITCHAIN_STRING:
                    for l in lens:
                        n = int(l)
                        r = lens[l]
                        # print(n,r, type(n), type(r), int(nelems*r))
                        numrecs = int(nelems*r)
                        logging.info('Generating numrecs= %s with n=%s digits', numrecs, n)
                        for i in range(numrecs):
                            dummy_str = fake.pystr(n, n)
                            dummy_content.append(dummy_str)

                if t == constants.FITCHAIN_FLOAT:
                    for l in lens:
                        n = int(l)
                        r = lens[l]
                        numrecs = int(nelems*r)
                        logging.info('Generating numrecs=%s with n=%s digits', numrecs, n)
                        for i in range(numrecs):
                            dummy_float = fake.float_with_n_digits(n)
                            # dummy_float = fake.pyfloat(1,2)
                            dummy_content.append(dummy_float)

                if t == constants.FITCHAIN_BOOL:
                    for i in range(nelems):
                        dummy_bool = fake.pybool()
                        dummy_content.append(dummy_bool)

                ###############################
                # Fake complex types
                ###############################
                if t == constants.FITCHAIN_EMAIL:
                    for i in range(nelems):
                        dummy_content.append(fake.email())

                if t == constants.FITCHAIN_ADDRESS:
                    for i in range(nelems):
                        dummy_address = fake.address()
                        dummy_content.append(dummy_address)

                if t == constants.FITCHAIN_NAME:
                    for i in range(nelems):
                        dummy_name = fake.name()
                        dummy_content.append(dummy_name)

                if t == constants.FITCHAIN_DATETIME:
                    for i in range(nelems):
                        dummy_time = fake.time()
                        dummy_content.append(dummy_time)

            # Fill dataframe by column
            data[field['name']] = dummy_content

        # Convert to dataframe and return
        # df = pd.DataFrame(data=data)
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        df.reset_index(drop=True)
        logging.info('Generated data %s', df.shape)
        return df


def _load_dataset(file, schema):
    if file.exists():
        if schema["type"] == "record":
            if schema['format'] == 'pandas.dataframe':
                return pd.read_csv(str(file.as_posix()))

        elif schema['type'] in ("PNG", "JPEG", "JPG", "BMP"):
            return Image.open(file)

        else:
            raise ValueError("Unknown schema type " + file['type'])

    else:
        os.makedirs(os.path.dirname(file), exist_ok=True)

        if schema["type"] == "record":
            if schema['format'] == 'pandas.dataframe':
                result = _generate_csv(schema)
                result.to_csv(file, index=False)

                return result

        elif schema['type'] in ("PNG", "JPEG", "JPG", "BMP"):
            img = _generate_image(schema)
            img.save(file)

            return img

        else:
            raise ValueError("Unknown schema type " + file['type'])


class FitchainDataProvider(BaseProvider):
    """ Create new provider class (fitchain customized) """
    def integer_with_n_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return random.randint(range_start, range_end)

    def float_with_n_digits(self, n, gt=1, lt=10):
        return round(random.uniform(gt, lt), n)

    def string_with_n_chars(n):
        strlen = random.randint(n)
        dummy_str = (''.join(random.choice(s.ascii_letters+' ') for i in range(strlen)))
        return dummy_str


class DataSetTree:
    def __init__(self, schema, root):
        self.schema = schema
        self.root = Path(root)
        pass

    def list(self):
        return self.schema['files']

    def open(self, path):
        if path not in self.schema['files']:
            raise ValueError("Path not found in dataset tree")

        fileschema = self.schema['files'][path]

        file = Path.joinpath(self.root, path)

        return _load_dataset(file, fileschema)


