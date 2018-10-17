(Transcript from Code Institute Tutorial)

# File Input/Outupt

In this unit, we're going to have a look at file input and output or I/O for short. Most programs store data in memory while they're running choosing the correct data structure can make all the difference to the performance of a program. A skilled developer knows how to use and combine smaller data structures into larger and more elaborate models in memory. But as great as these models are, anything held in RAM, or Random Access Memory, is volatile. That means that when the program shuts down, either by deliberately exiting or as a result of a crash, then the data is lost.

Also, as data gets more and more elaborate, some programs just can't store all of the data they work with in memory at the same time. Now, this is changing. Memory capacities are growing and the cost is continuing to fall, but to be safe, a persistent store of data on a non-volatile hard drive, solid-state
drive, flash memory or some other storage device will continue to be a part of computing for the foreseeable future. In this module, we're going to have a look at how to store data on a disk using files. You'll already be very familiar with files from your own operating system, and there are other ways of storing data - for example in a database - and we're going to have a look at that in future lessons. But even that usually just amounts to storing data in files and accessing them in a certain way.
Our learning outcomes for this module include: Reading from and writing to a file; relative versus absolute file paths; file modes, file handles and file types, and our walkthrough project is a quiz game.

# Reading from a File

## What is it?

How to open a file for reading in Python

## What does it do?

Opens a file in memory so that we can read, display and manipulate the contents.

## How do you use it?

Using the Python 'open', 'read' and 'readlines' methods.

LESSON:

In this unit, we're going to look at how to read from a file. So, create a new
Python project in Cloud9 and call it file_io like we have done
here. Then, when our project is open we want to initialize an empty git
repository and remember to add and commit your files as we go along. Now
we're going to create a new text file and call it data.txt. In that file we're
just going to add four lines of simple text. This is the first line, this is a
second, here is the third line and here, the fourth. When we've done that we
can save our file. Then we're going to create a new Python file and
call that quiz.py. So, in our python script we want to add the following code.
We want to define a variable f and it will open our data txt file for
reading. Then we're going to call the readlines() method and put that in the 
variable lines. We'll close our file handle and then we'll print the results 
to screen. When we save and run this, our output will be as follows. 
The code opened the file, read the lines into a variable called lines and as 
you can see, we have a list of strings. We can also see that each one contains 
a newline character, which is the \n and this makes sense because the file contains four separate
lines. The readlines() method splits this at those newline characters to
create a line of strings. If we modify it slightly and use the read() method instead
of readlines(), then see how it changes. Now, all of the data is read into a
single string including the newline characters it now appears just as text and
not as a list of strings. The newline character causes the string to be
displayed over the four lines of our file. A very simple practical thing
we can do with text files is to count the occurrences of words. The Project
Gutenberg website provides books that are out of copyright in text format.
For this example we'll use "The Secret Adversary", by Agatha Christie. So,
open up the link below as we are doing here, and select some text. Take about a
page of it. I'm going to copy that, and then we'll create a new file in our
project, which we're going to call book.txt. Then we can paste our text
into it. Save that and then create a new Python script called book.py.
Here we're going to use two standard libraries: the first one is the re
library for regular expressions, and the next one is the collections library that
allows us to count the occurrences of words. Now we'll put everything on one
line. Here we'll read everything into a string called text use the read() method.
Have it all in lowercase, and then we're going to use the regular expressions
findall() method with the pattern here - we'll explain that in just a minute -
and our text string. Finally, we're going to use the counter() method from our
collections, and we're also going to find the ten most common
words. So, let's save that and run it and see what result we get. Now, notice
that the entire contents of the file have been read into this string called
text, and then notice afterwards that the findall() method is used to pass that string
and find words. We don't have time to discuss everything about regular
expressions here, but the findall() method ensures that all occurrences of the
pattern are found. The pattern we're using is \w+
The w denotes anything that's not a whitespace, and the plus denotes one or more. So, for every
occurrence of one or more characters that are not whitespace, we view that as
a word. We may get some false positives - it's not perfect but it works fine for
our purposes here. Then, the counter() method from collections counts how many
occurrences there are and the most_common() method limits the results to ten
words. We see that we have then a list of tuples, where each tuple contains
the word and the number of occurrences. So that is how to read from a file! In
our next unit we're going to look at relative versus absolute paths.

# Relative and Absolute Paths


But, there's nothing to stop us from opening files in other directories too.
So, let's do this. Let's create a subdirectory in our project called "files".
There are a couple of ways of doing this. We can right-click on our project and
then go down to New Folder at the bottom of the menu, or we can do it in our
terminal window by typing mkdir and then "files" - the name of our directory. When we
do this, we'll notice then that "files" appears in the left-hand pane of our
Cloud9 window. So, let's create a new file in there - a text file. We're going to call
it relative_data.txt. Then let's add some content to it. For lack of
imagination, I'm just adding lines 1, 2, 3 & 4. We'll save that, and then we'll
modify our quiz.py script to open it. First we supply the name of the
subdirectory which, in this case, is files and then /relative_data.txt
Let's save this and run it to check that it works. Here
we can see that our content is returned from our relative_data.txt file just
as it was before. This is what's known as a relative path it identifies the
location of the data file relative to the script that's currently running.
It starts in a given location - the working directory that we're in - and
works down from there. By contrast an absolute path starts at the very top of
the file system. An absolute path is not relative to the running program but
rather it's a fully formed path to a specific file. We can demonstrate this by
going to our terminal window and changing into the files directory that
we created earlier. So let's do that now. We'll clear the screen first. Change into
our files directory using CD, and now we're going to use the PWD command, which
is short for Print Working Directory. We can see that this gives us our
current location on the file system. We can also find the absolute path of an
individual file using the readlink command here with the -f switch.
We'll use it, and then find the absolute path to relative_data.txt. There we
can see where it is on the file system. So, let's just try this. Let's take a copy
of this, put it into our quiz.py files to open it and see if it works.
We'll also just change back up to the previous directory that we were in so that
we can run our script. We'll paste that in there, we'll clear the screen and
we'll run our script just to see if it's working - and indeed it is. So, we can see
that to open a file using an absolute or a relative path is very straightforward
in Python. We just specify the path in the open command. We don't need to do
anything else. Generally speaking, though, if you can refer to a file using a
relative path then do so. Absolute paths couple applications very tightly to the
file system. It's normally unnecessary to rely on a
file being in a specific location like that. An exception might be where there's
a dependency on a third-party file. For example, in our boggle project, Mac users
could use the built-in dictionary that comes
pre-installed on that machine. That's a scenario where using an absolute path
makes sense because it avoids the need to distribute a dictionary with the app.
But if you do use absolute paths, make sure that they're easily changeable.
if Cloud9 moved this project to a different server or changed their file
system, then trying to open our relative_data.txt file with an absolute path
would no longer work. So, declare them as constants in your code or - even better -
keep them in a separate configuration file in your project or in an
environment variable. Now that we've seen how to open resources using absolute or
relative paths, in our next unit we're going to look at how to write a file in
Python