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
import base64
from io import BytesIO


img_str = b'/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC\
4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABlAJYDASIAAhEB\
AxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0f\
AkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2\
t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcF\
BAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpan\
N0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRA\
xEAPwC2bPTIE8028IOcZ2ZJP86khuLYF0RFVlGdhTBqlchyAC20pJvR+wPvVKW4ZLj7RNKmQm3A6c9aVPnlH3lZjfsuX4tTWi1dLgHZbv8AL1PbNStcuxBT\
pzz1xWfpMqLI6b1HPXoMVviKKdMRrn3Arkc6j67f1Y3VGCMdb+6NvcEzYkSUhQBgEDFXdKmluofPkb5pOiegqnqOlyxSCWNGXa25gRw9Q3Ot/YreRwqqUU4\
HSuim4zfMt+xz14uM720Oqd\
4raHYXRT6k1z19e3V1mLSolkwcSXD8In09T9K5nRL+y8QSPc3qXlzNnHlYbYPpjg13tk7+WkEenPDEowM4GPwrd029jBzS0Z5p4jV1hjguFzKkgYP1yc11d\
raC60mONlb7owccg10sGmWLSEm3RpjksXGe9XJ2g0yASyNEoP8AAOT+VYVaC3m7F06za5YK55vFYaiLuRJbaVUzjzfujHr/APWrr7NEigQlEJHAB9qytR8U\
QXd1NDE37qLABPHmEn+lWIbsSwbldwB/crzv3cZ+6zuoYd04Xas2Q6xqk0MJU2SKpHJ56frWLplhcXwnS02iWZflBPGfrW3crFNG43yhsffPI/Gm+HYnt9U\
SQsqxDhT0BNa2U2bS/hyXkY48Ga15wNxEjAf9NCRWpDoGoW8bmNbdZXGDjk4ruZZ5QcFsc+nXNR7AHy3PvXW8BTa1X4nguXY4qbTtSXy0aLz1HqR8lUpINS\
khe3hheGMtzvwFOPpXoMyxsnPGen4VmS2zpbzTJ83PygVjLLKLWmhcXZ9zgNS8E3OoSpKL6NGAwSUJzRXXBWuEDJlCc5HSiuaWDx8XywkrHpQxlBRSaZOvh\
KxmIWea5kA/vzEZ/LFNPgrw\
+JN32FJCRg+YS3867lLK3Uf6rkcZx61HPbbIZFRWJ9K9lVFeyPOdJqO55dq9mNM1TEa4gwu0fSug07UWNuGRVhTHByOaua7p8d3YeZtyydfoa5DT4/JuSHX\
zEB45z+lefVj7Oo13PUoNVKKb3R1st6snDtCy+ozmsO5trD7alxNbRTMnK+YK0BcK2FWJATx0qlf2QlBZ22sPToa5qlTl95bmsIKXuvYZJ4ntre5S0tbTbI\
p+cYAArWOthLuMIEEki8Z56+1cett5M4BbJc8Oas3Fv5iI7KwlLKcD7xPYColjq8tpFLA0Fujclub2aF3jTanO7YME49azb+e4gEEiRZDDbKAM4xXZeHLF5\
LpFkTcskeGHXnms25sTZJftJExCOWGOpAGKzn7SaU5Ns0punBuMVY5a5so3uUm2qAeTjuRWjZFIhtZfSmREXWnR3iNuQ5UORg96mS3YYJ9Bg/SsNVqbbqxbn\
iF5HgtxwMcdPQUtvZs86JIiNHAQ4B/gIpqI6kM38PIxVxZTBaSKjYdgRvPYkVvTrW3MZU9LG0AXj3J8wIGM9qUrkEDrxn61V0y5DWMaOqrKqgHB4OKtNIFH\
zsoBr6KlNVIqSdz52rF05OL\
I3gZ/m/yao3DSp8obv0PStFLgf8B7VRuSHILrxmqkn1FFrSzM9mjW6dpVwWAO30oqPVgYrkYXKsoINFRF6G7Wp1jyzQRurwyuxOF2PkYqCKO/kGXh2KOgLn\
NbAKL9yLB9cU15B1llUD0HWpU30RMoX3ZnPbKlpJJK2cA/J2rz6/sozJNchHtQjbSDwCf8K9DvpEnCIn3AeawNbjt1IguV+ScfI/bd6GsMXG9NTe50YOoo1\
HBbMx9OkEcJ3MjMfTIqSeUuhCr8vp9KbbWSwJsTdgDjk5q1HZF8549zXiV5NuyPXhFIx0t/Nfey884qa0tvtGreVvxKIzj2JGM1LOChR42UxK3zEUpiez8T2\
94i5glTr71FNdy5M7L4eWs8Fi8d1uM8cjAlvetnWdD87z5YhuEo+ZPfB/nVfwzqKSSPARg5zn1rqSQR7V7FKEZU0jzKk5Ko2eQf2QbXQLjThwybjGenfIrN\
gmeXRIZHiYyiXaQPY12mu6ZNJrDtBu2vjj864zVfE2n+Hrg6XDbTXN8DkW8SFjk98CuCdJ8zSOynUui88+y4gVujDJGKmEsUhkKMowe/euVKeMLw+fLbW+n\
RMcqkpy5/DtVu11O5hnS01C\
FWmfG0w8j8aylSaNlJM1Z53sZhMv3QcnHauutr+LUdKS7hZBLyAMA815Trs9xpd3mWZ3hkOCHHAFdp8OES8sroSbpFSUbcdMEV14JuE7PZnHjaanT5luabC\
4bl2XPsaJLdnhdj1GSBXR3tnF9k2oihh0rB3BCQenv617XPzrQ8X2fJLUw7yRJkjjmXDJnBPoe1FR6rEZWRkxnnOaKhwTZuqmh08s0uEDF2BJPHpQwH8PJB5\
+lBLDg/SrFvZST/ADbtq1s7JXORXk7IgAI2D5eOvvWPriQSPC0nPkncBnvXTzWNvBGWeZga8+8R3aJegq7bRgAeprz8wrL2XLHdnoYGhJVeaXQvW0pbDlc8Z\
wD2qeS7lkQpGiqCMEmuVmu7qSSOztpVTdyxzgmrGr3Ooi1+xww5dgFEwzXhqm2e02tiV9f0fR53S8vYkVuSh6VG3xM0CTEcEU1winllgYgD149KytM0i30yd\
JH09ZJurTXWHyfb0/GvSdAaS+KRTWVu0Zx9xAOK6aah8K1Mal92bOhW1tJaQ3lk++OVQ4cdCDXURKRGA/Ws2y0tNJhkW3c+U5LCM9FJ9KvQzB898V6lOKijg\
m7vQhvLNZEd0C+b/Dn1r\
kfCuioTqFzNYiDU5ZmaV2Tr2HP0FdncShYd3pUsDBoQw5zSlTUpXGpuKseXa/ok7zvv83IPAHzF/wDAVT0TQJLKOa6ubdomc8ZOWx6n0+lemapHbyQl3ZVI/\
jNeS+I9X1GO6KWiO0SnAIJCn3NclTDpO50QrNqxDrtlHqUHkQNlzyce1XPhnA9pfX0Tq+1NuQcggj+dZ+jx3c8xnmdRnrk//qrqNInjtbh2jbBbnJ71VKHvIm\
rO0GjrLm7iKBXdC2eMelYt95TyBo1bkYJPrUpO5tx5zzn61VmwRzXrxpqJ40qrlozNu4NoBXlifrxRU7skgCyLwvTHFFZu6ZrG1jVlJkkB7Zz6VvR4SAFewrn\
yM9OlatvOGsTn+Ec59qusvdIoS1fc5/XbzbvkZ+egFeb6tK0l1HJJzFyCP9qul1i6aW4JH3SxA+lZFzGs+Ie54FfP16rqVW+h72HpKnT8zE0sS3OspKUbYOB\
mvR4Jk8vy5djDpjnI/E1zejaJCT50srgocEDpTNeublUKW9uxUfL5pPOPar5WkrkylzS0Ni7s9Ge7DxXzrITzGTuz+Fd/4X06O0tRIu0bhwBkcV5D4e0qVnFxIzvJ1y47fU1634eV\
1gBmbK9iDwK6qFNRdznrVG9LnSuVZDnaQK4/UfEtnpV3Os13FAE/1nmkLsH410r3McfJlXjt3rnPFmmaLr9oE1K1WTZyso4YfjXRNO2hnTcU/e2MDxD8QbLT\
LUySO82cFUhwS+f0/Guq8K3t5e+H47+6iaET8wxH7wTtu9z6V43/AMI/DB4wtd8qNp8Cho0c8uF6L+B5r01dfGwKFcgAcdqzhe95G9ZwslE6i7ETWpDOqsw7\
8157qf2UXREm0lTj/Vlv/rUmueK5GkjsrREM7YyQclRUov5blwzysGACkJgj/vlhinJ3MbNasp+epTajyoOwEaLVWW/ggm2faJQVwfuCtOYxW8O52RnPCoSY\
3J9uxP0rh4dVW+up4ZXmgmQkNFdR8dexGDj3IrCpflNaSuz1XTmWe1SbepDDuMdahu4CqlSuSR1A4zUHhqUvpse5V247HIP41dmleYhEVsnsOlelRlJxTPKr\
RipNHO3jPBawShwu/IOfWit3Uba1uFj82DzCOoHUGin7RdUUqOg4BmO3ue1QXs729lOA3BWtOHYEDDbn1NYniFwbQ7WwCcGjETtTlp0Iw8f3kTlJ3beMLn6m\
qaOv2gybWJQEkdKsSoF\
Mbbvzpm0DzHKZQDj05r5pLU+kT0NfQb0XuXRNkinGD/GPpW9JJbTEeZbIXX2HH9BXnD3d3Z3SPbP5a5GR3Pt7D2FdlYajFqQEaMpfuPf/AAr1aTTR59WLTui\
/5qu+y3t0B/vnkge3YVo29yLNHM26dj13ueMfy+lQIqRDy4mXefvSelVZH2ZC8oOmf4zWuxgW5vE6RDY8qweiKOn41zeo+K4ZC6QI9zN2A5Gfr0q/MkUwKyIr\
euR3NVhZW4OUiA+gp3KTSOMl0e71C7+2XDsJv4cEgIPQVdisNT8vyV1GZYzwehNdSYoUAz+NV3lgjbYHxnpUtGjqNlLT9OgsE2oreYeTIeTn3rSLpEhmm2rt7\
f4f4Vj6jrtnpsJeZ1D/AMKZ5c+1c5eanPq3zPvRQceXmobtqEU5blrxBrMurf6KYl+y84JG7n3B4qvo0sxc213Es0WMAg/c/wB09R+Bx7VJFbmYcr838Xv7/\
WtaxtLS0CGQO248cHGaylJyRvFJbHSeEgbe3kRH3R7uM9fxFdC/HB+RyOnaud8NoI9SuE2tsOMZHGK6meNWj3lVDYwM+grvw0v3aR5eKg/aNoy2jlZzgtnuK\
KnijMkhG5lAHY0V0s\
wS0JkOQV6ZrJ1rLWEpJ+63H50UVOJ/hS9CcP8AxY+pgxRcLls5PcVBP81zIp+6vQdvyoor5k+liaEejw3EIlLYYDIwo64rPeD+ybcSwuzO6u5Lei4wv0J5P0\
oorvp6HJU3+Y5/EVxZ6fHIYxI0uWYk46Gri65JLEjGFR85GM+goorrWxzMJ9QkVdwUcjNZf9s3LAHgZzRRUjSGfa5pGKs/FBcJbtIV3FQSMmiikijgYrmTXt\
Xnubg7VicxpGOQMd66WzgXH5UUVnV+Jo36HU6Pp8MjZbnFSam7QXKBNuwNjbj9aKKznpBjh8RHFNJaatGVdiWIU88Y+ldnJMxiHoVHFFFdeAd07nDj+hUMjRs\
SO9FFFd7RwrY//9k='

# preload image background
# bg = Image.open(os.path.join(parentdir + "/data", 'happy_cat.jpg'))
bg = Image.open(BytesIO(base64.b64decode(img_str)))
bg_w, bg_h = bg.size


def open(schema, file):
    return _load_dataset(file, schema)


## make OBSOLETE
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
    # print('w=', w, "h=", h)
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

    if schema['format'] == 'csv':
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
                        numrecs = int(nelems * r)
                        logging.info('Generating numrecs=%s with n=%s digits', numrecs, n)
                        for i in range(numrecs):
                            dummy_int = fake.integer_with_n_digits(n)
                            dummy_content.append(dummy_int)

                if t == constants.FITCHAIN_STRING:
                    for l in lens:
                        n = int(l)
                        r = lens[l]
                        # print(n,r, type(n), type(r), int(nelems*r))
                        numrecs = int(nelems * r)
                        logging.info('Generating numrecs= %s with n=%s digits', numrecs, n)
                        for i in range(numrecs):
                            dummy_str = fake.pystr(n, n)
                            dummy_content.append(dummy_str)

                if t == constants.FITCHAIN_FLOAT:
                    for l in lens:
                        n = int(l)
                        r = lens[l]
                        numrecs = int(nelems * r)
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


def _generate_file(schema):
    if schema['type'] == 'image':
        return _generate_image(schema)
    elif schema['type'] == 'record':
        return _generate_csv(schema)


def _load_dataset(file, schema):
    if file.exists():
        if schema["type"] == "record":
            if schema['format'] == 'csv':  # 'pandas.dataframe':
                return pd.read_csv(str(file.as_posix()))
        elif schema['type'] == "image":
            return Image.open(file)
        elif schema['type'] == "collection":
            pass
        else:
            raise ValueError("Unknown schema type " + file['type'])
    else:
        os.makedirs(os.path.dirname(file), exist_ok=True)
        if schema["type"] == "record":
            if schema['format'] == 'csv':
                result = _generate_csv(schema)
                result.to_csv(file, index=False)
                return result
        elif schema['type'] == 'image':
            img = _generate_image(schema)
            img.save(file)
            return img
        elif schema['type'] == "collection":
            print("This is a collection of datasets or files")
            print("Generate the files you need")
            tree = DataSetTree(schema, './')
            return tree
        else:
            raise ValueError("Unknown schema type ", schema)  # + file['type'])


class FitchainDataProvider(BaseProvider):
    """ Create new provider class (fitchain customized) """

    def integer_with_n_digits(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return random.randint(range_start, range_end)

    def float_with_n_digits(self, n, gt=1, lt=10):
        return round(random.uniform(gt, lt), n)

    def string_with_n_chars(n):
        strlen = random.randint(n)
        dummy_str = (''.join(random.choice(s.ascii_letters + ' ') for i in range(strlen)))
        return dummy_str


class DataSetTree:
    def __init__(self, schema, root):
        self.schema = schema
        self.root = Path(root)

    @property
    def files(self):
        return [(dict_file['basename']) for dict_file in self.schema['files']]

    def __repr__(self)->str:
        """ Print this tree as a list of file paths """
        res = '[%s]' % ', '.join(map(str, self.files))
        return res

    def __get_files(self):
        return self.schema['files']

    def get_file_by_basename(self, name):
        """ Return schema of the first file with name """
        return [i for i in self.schema['files'] if i['basename'] == name][0]

    # FIXME
    def open(self, path):
        if path not in self.files:
            raise ValueError("Path not found in dataset tree")
        fileschema = self.get_file_by_basename(path)
        file = Path.joinpath(self.root, path)
        return _load_dataset(file, fileschema)

    def load_data(self, schema):
        return _generate_file(schema)

    def generator(self):
        """ Scans all files in this tree and generates their synthetic version """
        for schema in self.__get_files:
            dat = _generate_file(schema)
            yield dat
