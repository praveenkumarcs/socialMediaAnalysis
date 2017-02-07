# using  regular expressions

import re
from string import punctuation

def  processTweet(tweet):

	# Convert the string into lower case

	tweet = tweet.lower()

	# Remove the punctuation 

	tweet = tweet.strip('\'"?!.')

	# Remove the URLS and replace with word URL

	pattern = r'(www\.(\S+)\.com)|(http|https)://(\S+)\.com'

	regex = re.compile(pattern,re.IGNORECASE)

	tweet = re.sub(regex,"URL",tweet)

	# Remove the Handles such as @Username

	pattern = r'@(\S+)'

	tweet = re.sub(pattern,"USERNAME",tweet)

	# Remove the HashTags such as #Virat , #Happy and replace with the word in the hash tag

	pattern = r'#(\S+)'

	tweet = re.sub(pattern,r'\1',tweet)

	for char in punctuation:
		if char in tweet:
			tweet = tweet.replace(char,' ')  

	# Replacing multiple white spaces with single one

	pattern = r'\s{2,}'
	print tweet

	tweet = re.sub(pattern,' ',tweet)


	return tweet


if __name__ == "__main__":
	processTweet("i #like this restaurant@team.. www.google.com!!!!!!.......")


















