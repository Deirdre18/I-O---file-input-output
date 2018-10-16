#We want to define a variable f and it will open our data txt file for reading. Then we're going to call the readlines() method and put that in the variable lines. We'll close our file handle and then we'll print the results to screen. When we save and run this, our output will be as follows. The code opened the file, read the lines into a variable called lines and as you can see, we have a list of strings. We can also see that each one contains a newline character, which is the \n and this makes sense because the file contains four separate lines. The readlines() method splits this at those newline characters to create a line of strings. 

#A very simple practical thing we can do with text files is to count the occurrences of words. The Project Gutenberg website provides books that are out of copyright in text format. For this example we'll use "The Secret Adversary", by Agatha Christie. So, open up the link below as we are doing here, and select some text. Take about a page of it. I'm going to copy that, and then we'll create a new file in our project, which we're going to call book.txt. Then we can paste our text into it. Save that and then create a new Python script called book.py.

#f = open('data.txt', 'r')
#lines = f.readlines()
#f.close()
#print(lines)


#If we modify it slightly and use the read() method instead of readlines(), then see how it changes. Now, all of the data is read into a single string including the newline characters it now appears just as text and not as a list of strings. The newline character causes the string to be displayed over the four lines of our file.

f = open('data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

