import json
import dummy_data as dd
import sys

def generate(schemaString, targetFile):
    """
    Generate some dummy data based on the given schema string
    """
    schema = json.loads(schemaString)

    dummy = dd.DummyData(schema)
    dummy_df = dummy.generate_data()

    dummy_df.to_csv(targetFile, index=False)

generate(sys.argv[2], sys.argv[1])