import createTrainSet
import featureVector
import preprocessTweets
import cPickle as pickle



def verifyClassifier():	
	testTweet = 'horrible way is to feel worse  bad about yourself'
	processedTestTweet = preprocessTweets.processTweet(testTweet)

	with open('naiveBayes.pickle','rb') as f:
		NBclassifier = pickle.load(f)
		result =  NBclassifier.classify(createTrainSet.extract_features(featureVector.getFeatureVector(processedTestTweet)))
		print result
		
if __name__ == "__main__":
	verifyClassifier()