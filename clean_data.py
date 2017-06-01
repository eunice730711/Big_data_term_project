
# coding: utf-8
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import io
conf = SparkConf().setAppName("building a warehouse") 
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)

wordcount = sc.textFile("data_try.txt") # Read file
# stopRDD = sc.textFile("./data/stopword.txt") 
# stopList = stopRDD.map(lambda x: x.strip()).collect()
targetList = list('"().,?[]!;:|-1234567890') + ['/'] # deleted punctuation
# stopwords = list([u"推",u"噓",u"了",u"是",u"就",u"吧"])
def replaceAndSplit(s):  # Replace punctuation with blank space 
	for c in targetList: 
		s = s.replace(c, " ") 
		s = s.lower()
	return s.split()

def filterStopWords(line):
	with io.open('./data/stopword.txt','r', encoding='utf-8') as sw:
		stopwords = [word.strip('\n') for word in sw]
	for i in line:
		i = i.encode('utf-8')
		if i in stopwords:
			print i
			line.remove(i)
	return line



cleanRDD = wordcount.flatMap(replaceAndSplit) # call replaceAndSplit
cleanRDD = cleanRDD.map(lambda w : filterStopWords(w)) # call replaceAndSplit
cleanRDD.saveAsTextFile("outputfiles")

