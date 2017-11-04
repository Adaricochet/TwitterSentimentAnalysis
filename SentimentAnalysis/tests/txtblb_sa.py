from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
while 1:
	str=raw_input("Enter str");
	print str
	print TextBlob(str).sentiment


#print TextBlob("Samsung is very bad", analyzer=NaiveBayesAnalyzer()).sentiment

