
# Used for preprocessing of tweets
import preprocessTweets

#Get the feature vector 
import featureVector

#importing the language ToolKit
import nltk

#import the random to shuffle the dataset
import random

# Used to save the trained classifier
import cPickle as pickle

#import the twitter samples in NLTK corpus
from nltk.corpus import twitter_samples

#classify is used to find out the accuracy of the classifier
from nltk import classify

#wrapper class that has to be used when sklearn (external) classifiers are being used
from nltk.classify.scikitlearn import SklearnClassifier

#importing the external classifiers from sklearn
from sklearn.naive_bayes import MultinomialNB,BernoulliNB

#using the default class from classify's ClassifierI
from nltk.classify import ClassifierI

#find the mode using Counter
from collections import Counter


featureList = []
tweets = []
tweetmsgs = []


class VotedClassifier(ClassifierI):

	def __init__(self,*classifiers):
		self.ClassifierModels = classifiers

	def classify(self,feature):
		votes = []
		for classifier in self.ClassifierModels:
			vote = classifier.classify(feature)
			votes.append(vote)
		votesInfo = Counter(votes)
		return votesInfo.most_common(1)[0][0]

	def confidence(self,feature):
		votes = []
		for classifier in self.ClassifierModels:
			vote = classifier.classify(feature)
			votes.append(vote)
		votesInfo = Counter(votes)
		return votesInfo.most_common(1)[0][1] / len(votes)



def formTrainingSet():
	fileIDS = twitter_samples.fileids()	

	for fileid in fileIDS[:2]:		

		msgs = twitter_samples.strings(fileid)

		if 'negative' in fileid:
			tag = 'negative'
		else:
			if 'positive' in fileid:
				tag = 'positive'

		for msg in msgs:
			tweetmsgs.append((msg,tag))

	random.shuffle(tweetmsgs)


def extract_features(tweet):
	tweetWords = set(tweet)
	features = {}

	for word in featureList:
		if word in tweetWords:
			features[word] = True

	return features


def listOfFeatureSets():

	formTrainingSet()

	for msg,tag  in tweetmsgs:			

		processedTweet = preprocessTweets.processTweet(msg)

		feature_vector = featureVector.getFeatureVector(processedTweet)

		featureList.extend(set(feature_vector))	

		tweets.append((feature_vector,tag))



#if __name__ == "__main__":
listOfFeatureSets()		

TrainingSet = nltk.classify.util.apply_features(extract_features,tweets[:4000])	
TestingSet  = nltk.classify.util.apply_features(extract_features,tweets[4000:5000])

NBClassifier = nltk.NaiveBayesClassifier.train(TrainingSet)
#print 'Original nltk Naive Bayes Algo accuracy ==>',classify.accuracy(NBClassifier,TestingSet)

#testTweet = 'this movie is so sweet and delightful'
#processedTestTweet = preprocessTweets.processTweet(testTweet)
#print 'nltk Naive Bayes says tweet is :',NBClassifier.classify(extract_features(featureVector.getFeatureVector(processedTestTweet)))

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(TrainingSet)
#print 'MultinomialNB Algo accuracy is ==>',classify.accuracy(MNB_classifier,TestingSet)
#print 'MNB says the tweet is :',MNB_classifier.classify(extract_features(featureVector.getFeatureVector(processedTestTweet)))

Bernoulli_classifer = SklearnClassifier(BernoulliNB())
Bernoulli_classifer.train(TrainingSet)
#print 'Bernoulli_classifer Algo accuracy is ==>',classify.accuracy(Bernoulli_classifer,TestingSet)
#print 'Bernoulli says the tweet is :',Bernoulli_classifer.classify(extract_features(featureVector.getFeatureVector(processedTestTweet)))

hybridClassifier = VotedClassifier(NBClassifier,MNB_classifier,Bernoulli_classifer)
#tag = hybridClassifier.classify(extract_features(featureVector.getFeatureVector(processedTestTweet)))
#print 'hybridClassifier says the tweet is :',tag
#print 'confidence of classification:',100*hybridClassifier.confidence(extract_features(featureVector.getFeatureVector(processedTestTweet)))






















