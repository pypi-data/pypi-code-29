# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import codecs
from sklearn.model_selection import train_test_split
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score
import numpy as np


def read_data(folders_location,decode_type):
	"""
	Args:
	folders_location: string representing folders location assuming folder name is
	topic and content of folder belonging folders
	Output:
	decode_type: specify decode type to use
	"""
	folders = os.listdir(folders_location)
	X = []
	y = []
	for f in folders:
		files = os.listdir(folders_location+f)
		for fil in files:
			with open(folders_location+f+'/'+fil,'rb') as content:
				X.append(content.read().decode(decode_type).strip())
				y.append(f)

	data = pd.DataFrame()

	data['content'] = X
	data['topic'] = y
	return data

def tokenize(df):
	"""
	Args:
	df: dataframe that holds two data frames, content and topic.
	Output:
	df: dataframe with tokens column
	"""
	df['tokens'] = df.apply(lambda row: nltk.word_tokenize(row['content']), axis=1)
	return df
def stem(df):
	ls = LancasterStemmer()

	df['stemmed'] = df["tokens"].apply(lambda x: [ls.stem(y) for y in x])
	return df
def init_stop_words(strings):
	ignore_words = stopwords.words('english')
	ignore_words.extend(strings)

	return ignore_words

def bag_words(df,ignore_words):
	"""
	Args:
	df: dataframe that holds content, topic, and tokens
	"""
	f = lambda stemmed: Counter([word for word in stemmed if word not in ignore_words and word.isalpha()])
	data = (pd.DataFrame(df['stemmed'].apply(f).values.tolist()).fillna(0).astype(int))
	data['topic'] = df['topic']
	return data
def split_data(df,size,rs):
	"""
	Args:
	df: dataframe that contains bow score
	"""
	X_train, X_test, y_train, y_test = train_test_split(df.drop(columns='topic'), df['topic'], test_size = size, random_state=rs)
	return X_train, X_test, y_train, y_test
def encode_classes(df):
	le = LabelEncoder()
	df['topic']=le.fit_transform(df['topic'])
	return df
def run(folders_location,decode_type,strings,size,rs,model):
	ignore_words=init_stop_words(strings)
	df = read_data(folders_location,decode_type)
	df = tokenize(df)
	df = stem(df)
	df = bag_words(df,ignore_words)
	df = encode_classes(df)
	X_train,X_test,y_train,y_test = split_data(df,size,rs)
	model = model.fit(X_train,y_train)
	y_pred = model.predict(X_test)
	r2_ = r2_score(y_test, y_pred) 
	print(r2_)