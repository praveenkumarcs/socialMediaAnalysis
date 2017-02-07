# import re module
import re

#importing stopwords from nltk
from nltk.corpus import stopwords

#This is the script manually coded

import preprocessTweets

stopWords = stopwords.words("english")


def replaceRepeatingChars(word):
	prev,freq = word[0],0
	for char in word[1:]:

		if char == prev:
			freq += 1
			continue
		else:
			if freq > 1:
				word = word.replace((freq+1)*prev,prev*2)				
				freq = 0
			else:
				prev = char
	else:
		if freq > 1:
			word = word.replace((freq+1)*prev,prev*2)
	return word
		

	

def getFeatureVector(tweet):

	featurevector = []

	tweetwords = tweet.split()	

	mywords = ["USERNAME","URL","http","https"]

	allwords = stopWords+mywords

	for word in tweetwords:

		# Replace repeating characters with two instances 
		word = replaceRepeatingChars(word)

		pattern = r'^[a-zA-Z]\S*$'

		regex = re.compile(pattern,re.IGNORECASE)

		match = regex.search(word)

		if word in allwords or match is None:
			continue

		featurevector.append(word)

	return featurevector


if __name__ == "__main__":
	tweet = "this is the good tweet i have seen so far"
	finaltweet = preprocessTweets.processTweet(tweet)
	print getFeatureVector(finaltweet)

















