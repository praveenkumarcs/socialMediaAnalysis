import SentimentAnalysis as SA
from nltk.twitter import Twitter,credsfromfile,Query
import preprocessTweets 
import featureVector

Oauth = credsfromfile()
tweetlist = []


def grabStoredTweets():
	infile = open('twitter-out.txt','w')
	infile.close()
	infile = open('twitter-out.txt','a')
	client = Query(**Oauth)
	tweets = client.search_tweets(keywords='srinivas mummareddy',limit=25,lang='en')		
	while True:
		try:
			tweet = tweets.next()
			tweet =  tweet['text'].encode('utf-8')	
			tweet = preprocessTweets.processTweet(tweet)
			print tweet		
			tweetlist.append(tweet)
		except:
			break
	for tweet in tweetlist:
		FeatureVector = featureVector.getFeatureVector(tweet)
		features = SA.extract_features(FeatureVector)
		label = SA.hybridClassifier.classify(features)
		label += '\n'
		infile.write(label)
	infile.close()



	#keywords = raw_input('Enter The Terms you want to Search,Seperated by ","')
grabStoredTweets()
	
			

