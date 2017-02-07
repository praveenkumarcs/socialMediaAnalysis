import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

infile = open('twitter-out.txt','r')
words = infile.read().split('\n')
pos = words.count('positive')
neg = words.count('negative')
print pos,neg
objects = ('Positive', 'Negative','Total')
y_pos = np.arange(len(objects))
performance = [pos,neg,pos+neg]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('tweets')
plt.title('Sentiment Chart')
 
plt.show()

