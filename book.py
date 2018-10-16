#Here we're going to use two standard libraries: the first one is the re library for regular expressions, and the next one is the collections library that allows us to count the occurrences of words.

import re
import collections

#Now we'll put everything on one line. Here we'll read everything into a string called text use the read() method. Have it all in lowercase, and then we're going to use the regular expressions findall() method with the pattern here - we'll explain that in just a minute - and our text string. Finally, we're going to use the counter() method from our collections, and we're also going to find the ten most common words. So, let's save that and run it and see what result we get.

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))

#Now, notice that the entire contents of the file have been read into this string called text, and then notice afterwards that the findall() method is used to pass that string and find words. We don't have time to discuss everything about regular expressions here, but the findall() method ensures that all occurrences of the pattern are found. The pattern we're using is \w+ The w denotes anything that's not a whitespace, and the plus denotes one or more. So, for every occurrence of one or more characters that are not whitespace, we view that as a word. We may get some false positives - it's not perfect but it works fine for our purposes here. Then, the counter() method from collections counts how many occurrences there are and the most_common() method limits the results to ten words. We see that we have then a list of tuples, where each tuple contains the word and the number of occurrences. So that is how to read from a file! In our next unit we're going to look at relative versus absolute paths. 