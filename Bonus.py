"""
Author:             Sean Hannaway
SRN:                22039359
Date:               January 2024
Description:        This program is very similar to the previous except this time we have 2 arrays, a1 and a2. This program
                    outputs the most occured word in a1 that are not in a2 and if theyre are 2 or more instances of words
                    having the same count, the words would be then sorted alphabetically.
4. Bonus

"""
from collections import Counter  # used to count the occurences of elements of the array

# array of execrpt from book
a1 = [""" Momentarily he caught O’Brien’s eye. O’Brien had stood up. He had taken off his spectacles 
and was in the act of resettling them on his nose with his characteristic gesture. But there was a 
fraction of a second when their eyes met, and for as long as it took to happen Winston knew—yes, he 
KNEW!—that O’Brien was thinking the same thing as himself. An unmistakable message had passed. It was 
as though their two minds had opened and the thoughts were flowing from one into the other through their
eyes. ‘I am with you,’ O’Brien seemed to be saying to him. ‘I know precisely what you are feeling. 
I know all about your contempt, your hatred, your disgust. But don’t worry, I am on your side!’ And 
then the flash of intelligence was gone, and O’Brien’s face was as inscrutable as everybody else’s. 

That was all, and he was already uncertain whether it had happened. Such incidents never had any 
sequel. All that they did was to keep alive in him the belief, or hope, that others besides himself 
were the enemies of the Party. Perhaps the rumours of vast underground conspiracies were true after
all—perhaps the Brotherhood really existed! It was impossible, in spite of the endless arrests and 
confessions and executions, to be sure that the Brotherhood was not simply a myth. Some days he believed
in it, some days not. There was no evidence, only fleeting glimpses that might mean anything or nothing:
snatches of overheard conversation, faint scribbles on lavatory walls—once, even, when two strangers 
met, a small movement of the hand which had looked as though it might be a signal of recognition. 
It was all guesswork: very likely he had imagined everything. He had gone back to his cubicle without
looking at O’Brien again. The idea of following up their momentary contact hardly crossed his mind. 
It would have been inconceivably dangerous even if he had known how to set about doing it. For a second,
two seconds, they had exchanged an equivocal glance, and that was the end of the story. But even that 
was a memorable event, in the locked loneliness in which one had to live.

Winston roused himself and sat up straighter. He let out a belch. The gin was rising from his stomach.
His eyes re-focused on the page. He discovered that while he sat helplessly musing he had also been 
writing, as though by automatic action. And it was no longer the same cramped, awkward handwriting 
as before. His pen had slid voluptuously over the smooth paper, printing in large neat capitals—DOWN
WITH BIG BROTHER DOWN WITH BIG BROTHER DOWN WITH BIG BROTHER DOWN WITH BIG BROTHER DOWN WITH BIG BROTHER
over and over again, filling half a page. 

He could not help feeling a twinge of panic. It was absurd, since the writing of those particular words
was not more dangerous than the initial act of opening the diary, but for a moment he was tempted to 
tear out the spoiled pages and abandon the enterprise altogether.
"""]

# array of words to not count
a2 = ['a', 'the', 'of', 'and', 'to', 'in', 'that', 'it']

# combine all paragraphs of a1 into a single string and convert all text to lowercase
txt = " ".join(a1).lower()

# counts the words that are in a1 but not a2, splits a1 using whitespaces
words = Counter(word for word in txt.split() if word not in a2)

# retrieve the top word and its counts from words
most_freq_words = words.most_common(1)

# sort the most frequent words by count and if the same words have the same count by alphabetical
most_freq_words_sorted = sorted(
    most_freq_words,
    key=lambda x: (-x[1], x[0])
)

# output the result
for word, times_occurred in most_freq_words_sorted:
    print(f"{word} : Occurred {times_occurred} Times In The Paragraphs of 1984 by George Orwell")
