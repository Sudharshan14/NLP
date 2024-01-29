import nltk
import multiprocessing as mp
import time
import itertools
from utils.k_success import top_k_words, success_at_k, average_k
import os
import matplotlib.pyplot as plt
%matplotlib inline

nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet as wn
print("Total number of words in Wordnet = ", len(list(wn.words())))


birkbeck_corpus_data = []
with open('Data/FAWTHROP1DAT.643', 'r') as corpus_data1:
    for line in corpus_data1:
        data = line.split()
        birkbeck_corpus_data.append(data)
    
with open('Data/SHEFFIELDDAT.643', 'r') as corpus_data2:
    for line in corpus_data2:
        data = line.split()
        birkbeck_corpus_data.append(data)

birkbeck_corpus_data = sorted(birkbeck_corpus_data)
print("Total number of words in Birbeck corpus = ", len(birkbeck_corpus_data))

print(birkbeck_corpus_data[:10])


pool = mp.Pool()
start_time = time.time()
top_k = []
top_k.append(pool.map(top_k_words, birkbeck_corpus_data[:10]))
    
print("Parallelization Runtime: %s" % (time.time() - start_time))

print(top_k)

top_k_result = []
start_time = time.time()
top_k_result.append(pool.map(top_k_words, birkbeck_corpus_data))
print(top_k_result[0][-10:])

# Getting the success at k
success = success_at_k(top_k_result[0])
print(dict(itertools.islice(reversed(success.items()), 5)))

# Getting the average success at k
avg_success = average_k(success)
print(avg_success)

x = list(avg_success.keys())
y = list(avg_success.values())

# Plotting the line graph
plt.plot(x, y, marker='o', color='red', linestyle='-')

# Adding labels and title
plt.title('Average success at k', fontsize=14)
plt.xlabel('Top-k', fontsize=14)
plt.ylabel('Average', fontsize=14)
plt.grid(True)

# Adding data labels
for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')

# Saving the graph
plt.savefig('average_success_line.png', dpi=400)

# Displaying the graph
plt.show()

