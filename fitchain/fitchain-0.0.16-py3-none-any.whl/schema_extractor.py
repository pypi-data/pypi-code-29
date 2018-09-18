import json
import data_template as dt
import sys

def extract(sourcepath):
    """
    Extract the data template from the given file
    """
    print('Loading data and generating schema')
    df = dt.DataTemplate()
    df.load_data(sourcepath, )
    data_schema = df.get_template()

    if data_schema:
        print('### FITCHAIN SCHEMA START')
        print(json.dumps(data_schema, ensure_ascii=False))
        print('### FITCHAIN SCHEMA END')
    else:
        sys.stderr.print('no dataschema could be generated')

extract(sys.argv[1])
