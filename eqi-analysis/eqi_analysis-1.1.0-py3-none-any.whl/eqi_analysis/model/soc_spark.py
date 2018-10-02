import os
import pickle
import sys

from pyspark import SparkFiles
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from sparknlp.annotator import *
from sparknlp.base import DocumentAssembler, Finisher


class SOCClassifier:
    def __init__(self):
        with open(SparkFiles.get('soc_c.pickle'), 'rb') as file:
            soc_c_map = pickle.load(file)
        self._title_map = soc_c_map

    @staticmethod
    def jaccard(s1, s2):
        return float(len(s1.intersection(s2)) / len(s1.union(s2)))

    @staticmethod
    def argmax_jaccard(job_title, title_map):
        max_score = -1
        argmax = None
        for k, v in title_map.items():
            score = SOCClassifier.jaccard(v[0], job_title)
            if score > max_score:
                argmax = v[1]
                max_score = score
        return argmax

    def classify(self, job_title):
        if job_title is None:
            return -1
        return SOCClassifier.argmax_jaccard(set(job_title),
                                            self._title_map)


if len(sys.argv) != 5:
    raise AttributeError(
        "Mandatory arguments: "
        "[part] [driver_host] [hdfs_host] [output_folder]")

(part, driver_host, hdfs_host, output_folder) = sys.argv

spark = SparkSession.builder \
    .appName("soc_job_categorization") \
    .config("spark.driver.extraClassPath", "spark-nlp-assembly-1.6.0.jar") \
    .config("spark.driver.host", driver_host) \
    .getOrCreate()

soc_c = SOCClassifier()

df = spark.read.parquet(
    'hdfs://{}/job_hash_title_{}_cleaned.parquet'.format(driver_host, part))

document_assembler = DocumentAssembler() \
    .setInputCol("title")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

normalizer = Normalizer() \
    .setInputCols(["token"]) \
    .setOutputCol("normal")

stemmer = Stemmer() \
    .setInputCols(["normal"]) \
    .setOutputCol("stem")

finisher = Finisher() \
    .setInputCols(["stem"]) \
    .setCleanAnnotations(True) \
    .setOutputAsArray(True)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    normalizer,
    stemmer,
    finisher
])

out_df = pipeline.fit(df).transform(df)


def to_soc(rows):
    socs = []
    first_hash = None
    for r in rows:
        if first_hash is None:
            first_hash = r['hash']
        soc_line = ','.join([r['hash'], soc_c.classify(r['finished_stem'])])
        socs.append(soc_line)
    lines = '\n'.join(socs)
    with open(os.path.join(output_folder, 'part_' + first_hash), 'w+') as file:
        file.write(lines)


out_class = out_df.repartition(30).foreachPartition(to_soc)
