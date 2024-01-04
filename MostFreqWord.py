"""
Author:             Sean Hannaway
SRN:                22039359
Date:               January 2024
Description:        This program reads the paragraphs from the book 1984 by George Orwell, splits the words up through
                    whitespace and counts the occurences of each word. Each time a word occures in the text the counter adds
                    to that words counter and sends back the data its collected into a new .txt file, giving the information
                    of the top 5 words that occur most frequently in this text. The words are also ordered in the order they
                    appear in the text, if they occur the same number of times.


3.3 Most Frequent Word Problem
3. Write a Python program implementing your algorithm.

"""
from collections import Counter # used to count the occurences of elements of the .txt file

# open the code in read mode ('r')
with open('most_frequent_words.txt', 'r') as read_file:  # as easier to use than not to, if not used .close() needed
    txt = read_file.read().lower() # new variable txt created, reads and stores in txt and converts all characters to lowercase

# another variable words created and whatever data was stored in the txt variable is split using any whitespace characters and counter is used to count the occurences of the words
words = Counter(txt.split())

# get the 5 most common words and their counts of the words variable
most_freq_words = words.most_common(5)

# sorted function used to sort the most_freq_words list
most_freq_words_sorted = sorted(
    most_freq_words,
    key=lambda x: (-x[1], txt.index(x[0])) # sorts words in decesding order by count, then where the appear in the text
)

# write a new file named most_frequent_words_results.txt in write mode
with open('most_frequent_words_results.txt', 'w') as write_file:
    for word, times_occurred in most_freq_words:
        write_file.write(f"{word} : Occurred {times_occurred} Times In The Paragraphs of 1984 by George Orwell\n")
# Ouput the result of the for loop in the new .txt file