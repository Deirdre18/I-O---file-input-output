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

## What is it?

Relative vs absolute paths for file access.


## What does it do?

Defines where on a file system we store our files and how we access them; whether using relative or absolute paths.


## How do you use it?

Decide on the layout of your file structure, and determine which method is best for your project.

LESSON:

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
Python.

# Writing to a File

In this unit, we're going to look at how to write to a file in Python. So, let's go
ahead and create a new Python script in our project here. We'll call it write.py.
Let's open that up and add some code to it. So, again, we use f as our file
handle. We're going to use the open function and give it a file name, but this
time we're going to use the 'w' argument for write, instead of the 'r' argument
for read that we did before. Now, instead of read we're going to use
write to write something to the file, and then we'll close it again. So, just
thinking about that for a minute, looking at our access modes here - we're
going to discuss those in a little bit more detail later - but you could have
also put 'a' for append there. We'll have a look at that soon, but right now let's
just run our file and see what happens. So, first of all, as we can see over on
the left hand pane here a new file has being created. And, if we open that up and
have a look at the contents, you can see that it says Hello, which is exactly the
content that we wanted to write to it from our script here. But, what if we
change the content that we're writing here? Let's change that to 'World'. We'll
save it, we'll run it again, and now when we open our file
first of all Cloud9 is going to tell us it's changed and asks if we want to
reload it. So we will. Now it says World. Notice what's happened here that the
contents of the file have been overwritten! The content hasn't been
appended to the end. If we want the content to be appended to the end of the
file, then we need to change our file access
mode here from write to 'a' for append. Let's do that. We'll change our content
back to 'Hello',
save it. We're just going to run the file a few times, and we'll see what
happens. So, now, when we go into our newfile.txt file and have a look, we can
see that everything has been appended. 'Hello' has been appended three times
to the end of our file, but notice here that we don't have any new lines! It's
all run together as one script. If we want, we can include newline characters
if we want line breaks, and to do that we would just put \n which is
the newline character. We'll delete our file, and then we'll run our script again
just to demonstrate that this works. As you can see, whenever we delete it and
then run the script again the file is recreated. We'll run it four times now and
have a look at the contents again. So you have to reload, and now we can see that
the text is nicely presented with newline characters. Each run of the
program appends and writes to a new line. Now, remember before we used the
readlines method. We can also use the writelines method if we want to actually
write a list of strings. So, let's create a variable called lines and in this
we'll have our list. So, we're going to put 'Hello World, welcome to File I/O'. Okay,
and then we're going to change the function here to writelines. We're going
to use that method, and we'll change the content that we're writing here to lines
instead of actual text. So, again we're going to delete our newfile.txt
file. We'll save it, and let's just clear the screen here, and then run our script
again. So, now a new file has been recreated, what do we have this time?
Well, again, it's now written a string but we have no new line characters, but as
you can see the list that we gave has now been written. If we did want to add
newline characters in, then we could do that. We could put the newline character
at the end of each element here in our list, but the best way to do it is to
actually use the join method. So, that's going to join this into one single
string using \n as a separator. Now, instead we send text instead of
lines to our file. So, let's delete it and let's run our script again. And, this time
when we open it up and ask Cloud9 to reload it for us, then we can see that we
have everything on nice neat new lines. So, that's how to write a file in Python.
Our next unit will look at file access modes.

# File Access Modes

## What is it?

File access modes are the different arguments passed to the 'open' command.


## What does it do?

They allow the file to be opened for reading, writing, appending or a combination of these.


## How do you use it?

Supply different file access modes as the second argument to the 'open' command.


LESSON:

So, now we're going to take a look at file access modes. The second argument to
the file 'open' command is the access mode, which specifies the actions that can be
performed on the file when it's opened, such as reading, writing or appending
etc. You've already encountered these in the form of 'r', 'w and 'a' modes for
read, write and append. These are going to be the ones you use the most
often, but there are others, so we'll take a run through all of the
modes now. The first one, as we said, is the 'r' or read mode. This only allows you
to read from a file and if it doesn't exist, then it will throw an error. The 'w'
mode only allows you to write to a file and if that file doesn't exist, then a
new one will be created. The 'a' for append, that we've already come across, allows
you to append to a file, which means to write new content after the existing
content. Again, if it doesn't exist a new file will be created. The 'r+' mode is for
read and write. This allows you to read and write to a file. If it doesn't exist
it will throw an error. If it does exist, then its contents will be overwritten.
'w+' for read and write again is the same as 'r+', but a new file will be created if it
doesn't exist instead of an error being thrown. And, 'a+' is for read and append. This
is the same as 'w+', but the file is opened for append, so the existing content won't
be overwritten. 'rb', 'wb' and 'ab' are exactly the same as 'r', 'w' and 'a', but for binary data
instead of text. Now, you'll normally use 'r', 'w' and 'a', but since 'r' is used most
often then you can use open without the last argument and, if you do that, then it
means read-only. That means that typing this...is exactly the same as
typing this...

Now, these different file modes can be confusing, particularly when we're
opening a file for read and write, or read and append at the same time. So, in
the upcoming units we're going to explore these access modes in more
detail, but first let's look at how our position in a file is tracked while we
read and write its contents. We'll do that in our next unit.

# File Handles
 
## What is it?

File handles are Python objects that allow us to manipulate files.


## What does it do?

Creating a file handle object allows us to open files in order to read from them and write to them. We also use the file handle object to close an open file.


## How do you use it?

LESSON:

Supply a variable name when opening a file. This will become the file handle.


In this unit, we're going to talk for a few minutes about file handles. Now,
you'll notice in the previous units that we've used the variable 'f' to get the
results back from the open method. Now, 'f' is a variable. We could have called it
anything, we've chosen 'f' because that's nice and short and easy to remember, but
when you gets the results of the open function, 'f' stores an object, and this is
called a file handle. It allows us to manipulate our files. Attached to this
object are various methods that we use for reading and writing the contents of
our files. You can see what methods are available to you by typing 'f' and then
the full-stop in Cloud9. You'll see here we have close, we have read, readline.
We're familiar with these. There's a few others that we're going to learn
about a little bit later: seek and tell. We've also used write already as well. So,
this is how we access the methods that are attached to this new object that
we've created. Now, it's important to understand that when you open a file
you're reading or writing at a certain position within that file. When you use
the readline method - let's type it here - to read in a line, then what actually
happens is that your position within the file is advanced by whatever number of
characters are in that line. So, the next time you read a line the data will be
read from that new position. Lines are kind of an abstract thing anyway because
the file itself doesn't actually have any lines. The file is just one long
sequence of bytes, which is how the computer stores characters. When
Python sees a line separator such as the \n, then it interprets that as
making the break between two lines. So how does Python
track where we are in a file? Well, that's tracked using what's known as a cursor.
And, just like your position in a word processing document is represented by a
cursor that indicates where text will be inserted or deleted, then it's the same
with a file. In fact, we can use the cursor here as an example. If we put the
cursor in the middle of a line and start typing, then we know that that's where
the text is going to appear. Files use a cursor as well to track where they
are. Whenever we write or read file contents using the different file handle
methods, then that causes the cursor to move. You can move the cursor to a
specific position in the file using the method that we just looked at a few
seconds ago, the seek method, but we're going to have a look at that a bit more
in our next unit. We could continue using scripts to
demonstrate file i/o, but to really get a feel for how it works then we need
quicker feedback than we can get from just writing and running scripts. So in
the next lesson we're going to use the Python console or Python shell as it's
also known to manipulate files.

# Console File Access - Part One
 
## What is it?

Using the interactive Python console to manipulate files.


## What does it do?

The Python console gives us more instant feedback, so we can use it to read, write and append to files.


## How do you use it?

Open the Python console in the terminal window, and type in the commands interactively.

LESSON:

In this unit, we're going to have a look at how to access files from the Python
console. The Python console is an example of what's known as a REPL, R E P L
which stands for Read, Evaluate, Print and Loop. REPLs are an increasingly common
tool in modern programming languages. They're very useful because they allow
us to execute code in real time from the command line. We can then see and react
to results. We can manipulate variables and data in memory directly rather than
by having to write scripts and run them. So, to run the Python console simply type
python3 at the command prompt. As we can see, this opens the Python console.
Whenever we see the >>> arrows here, that indicates that we're in
the console and from here we can type Python code. We can declare then use
variables. Let's see an example of that now. If we declare a variable called 'x'
and give it a value of 20, 'y' and give that the value of 5 and then print(x - y)
then we can see in real time we get the value of 15. So, now that we know
the basics of using the console, let's use it to manipulate some files. So, we'll
do like we did in previous units. We'll declare a file handle 'f' and we'll ask
this to open a file, which we'll call data.txt. We'll use the 'w' flag because we're
going to open it for writing. Then we're going to write the string 'Hello,
World'.

Now, notice that the write command returns the number 11. That's the length
of the message that we've written. If you count the number of characters in 'Hello
World' including spaces, then we get the number 11. But, if we were to open the
data txt file now in our Cloud9 editor would we expect to see 'Hello World'. Well,
surprisingly it's empty! Why is that? Well, the reason is that the new contents that
we've written are in a buffer. They aren't actually written to the file
until we use f.close() to close it. We can trigger the writing of the buffer
to the file while keeping it open by using a method we haven't seen yet,
which is the flush method. So, if we run f.flush(), and now we open the data.txt
file, Cloud9 tells us that it's changed on the
disk. When we reload it, we can see that our contents 'Hello World' are now
there. So, now let's close the file using the close method. Similarly, we can append
to a file just the same as we would by writing to a file. We just change the
access mode. Let's do that again. So, we're going to open data.txt. This
time, we're going to open it in append mode. We're going to write 'Appended Line
1' and then we'll put a new line. We'll write 'Appended Line 2', and we'll put a
new line. Notice each time we do this, again, we get the length of our message
back. And, we'll do 'Appended Line 3' and we'll put a new line. So, again, these
are written, if we then close the file the contents of the buffer will be
written. And we can see, above in our editor, that the
file has changed and now we have our three appended lines. We can also read
files from the console as well this way. So, again this is a case of just changing
the access flag and using a different method. We'll open the file for
reading this time. We'll use the read flag, we'll then read everything from the file
into lines, and then we'll print the lines. So, there we have the content
of our file 'Hello World', and then our three appended lines. So, let's close that.
Now that we know how to read write and append to files we can use the Python
console to see what effect these operations have on the file cursor
position. To do that, we use the tell() method. So, let's open our data.txt file
for reading again. Now, we'll use the tell() method and that will tell us the
position of the cursor in our file. For a newly opened file, the cursor is always
at position 0. Whenever we read the contents of the file, the cursor position
is advanced. So, let's read the contents of our file and let's run f.tell() again.
And now we have 59 as our cursor position. This is useful because, using
another method the seek() method, we can move the cursor to a specific position.
For example, to move the cursor back to the start of the file we would seek to
position zero. This allows us to read the contents of the file again without re-opening
it. So, let's do that. We can see that it actually tells us where the file
cursor is now after we've run seek(), but let's run the tell method again just to
confirm that. Sure enough, our file cursor is at position zero. Whenever we
write to a file, it also moves the cursor. Let's close this, and let's open it again
for writing. So, remember to use the 'w' flag for writing. So, where is the cursor
now? Well, it's at position 0. If we do f.write("Hello")
we get 5 back because that's the length of our message. Let's do it again, f.write("World")
we get 5 back because that's the length of our message. Where is the file
cursor now? Well let's check it with the tell() method. It's at position 10, and let's
finally close our file. So, we can see that when we write to a file it advances
the file cursor forward. In our next video, we're going to have a look at how
the read and write methods affect the file cursor, and set some challenges too.

## Output from Console: 

~/workspace (master) $ python3
Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 20
>>> y = 5
>>> print(x-y)
15
>>> f = ("data.txt", "w")
>>> f.write("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'write'
>>> f = open("data.txt", "w")
>>> f.write("Hello World")
11
>>> f.close()
>>> f.flush()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> f = open("data.txt, "a")
  File "<stdin>", line 1
    f = open("data.txt, "a")
                         ^
SyntaxError: invalid syntax
>>> f = open("data.txt", "a")
>>> f.write("Appended Line 1\n")
16
>>> f.write("Appended Line 2\n")                                                                             
16
>>> f.write("Appended Line 3\n")                                                                             
16
>>> f.close()
>>> f = open("data.txt", "r")
>>> lines = f.read()
>>> print(lines)
Hello WorldAppended Line 1
Appended Line 2
Appended Line 3

>>> f = open("data.txt", "r")
>>> f.tell()
0
>>> text = f.read()
>>> f.tell()
59
>>> f.seek(0)
0
>>> f.tell()
0
>>> f = open("data.txt", "w")
>>> tell()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tell' is not defined
>>> f = open("data.txt", "w")
>>> f.tell()
0
>>> f.close()
>>> f.write("Hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> f.write("Hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> f = open("data.txt", "w")
>>> f.tell()
0
>>> f.write("Hello")
5
>>> f.write("World")
5
>>> f.tell()
10
>>> f.close()
>>> 


# Console File Access - Part Two
 
## What is it?

Using the interactive Python console to manipulate files.


## What does it do?

The Python console gives us more instant feedback, so we can use it to read, write and append to files.


## How do you use it?

Open the Python console in the terminal window, and type in the commands interactively.

LESSON:

In this video, we round out our discussion of file access from the
Python console. And, as we said, we're going to look at the read plus write
methods. Things get very interesting when we're using these methods if we don't know
what we're doing - and interesting is another word for confusing. So, to
demonstrate how these work, we're going to have a look at them now. We deleted
our data.txt file, so let's create it back again. And, we're just going to add some
content to it. I'm going to add three lines: Line 1, Line 2, and Line 3. I'm
going to finish this file with a new line and then save it. Ok, so now you can
run the following code - either in the Python console or you can create a
Python script - it's entirely up to you. By this stage you'll be comfortable with
both methods. I'm going to use the console just to keep doing what we were
doing before. So, let's open this file that we just created, for reading and
writing. Again, f = open. The file is date.txt, and we're going to open it
for reading plus writing. Let's read all of the content into the lines
variable again, and we'll print them.
Everything is doing what we would expect so far. Now, what do you think will happen
if we try to write to this file as well? Now, we said in the previous unit - in one
of the previous units - that read plus, which is what we've opened it as here,
overwrites the file. So if we write('Line 4'), and let's put a new line at the end
of it, then where would we expect it to be written? Well, let's close the file
and see what happens. As we can see from the example above, what actually happened
is that 'Line 4' has been written at the end of the file. Why is that? Well, the
reason is that we opened the file and the cursor would be at position zero. The
contents of the file were then read into the lines variable as we said, but
remember what that does. It advances the file cursor to the end of the file.
So, now when 'Line 4' is written to the file, it's written at the end because the
cursor was moved. Let's try a different example let's put our data.txt file
back to three lines and we'll save it. And, we'll do this again, but this time
we're not going to read the data in. So, f=open("data.txt") and we're going
to open it for reading plus writing. This time, we'll just add some text without
moving the cursor. Now what happens? Well, as you can see in the pane above, it's
overwritten the first line. The cursor is at the beginning of the file when we
first open it, but we don't do any read so the cursor doesn't move. When we write
the word like we have here, it overwrites the start of the file contents. Now, this
is important to know because, although we said that the read+ file access mode
overwrites the file, it actually overwrites whatever position the cursor is
at. So, if you've moved the cursor to the end of the file then it will actually
function very similar to an append. So, that leads us to ask, then, what does
append+ do? Let's change our data file back to Line 1, Line 2, and Line 3
and now we'll open it for append so open date.txt, and we'll open it for
append+. So, that's reading and appending. Now, at the moment let's just
see where our cursor is. It's at 21, right at the end of our file. So,
let's set it back to zero. So, now our cursor is at the beginning of the file.
Now, if we write some text again, where do you expect this to go? At the beginning?
At the end? Somewhere else? Well, let's close the file and have a look.
Interestingly, we see that this goes at the end of the file because, even though
we've actually made sure that the cursor is at the start of the file by using
seek, the new content was still written to the end of the file. That's the
big difference between opening a file for read + write or read + append. In
append mode, new writes always go to the end of the file. So, there's an
interesting benefit to using this append mode because that means that you can
move the cursor around within the file for the purposes of reading, but if you
need to add data on at the end then it will always be added with the append, you
don't actually need to move the cursor back to the end in order to get the data
there. As you can see, this behavior has the potential to be very confusing, so
take some time to have a look at these different file access modes and
experiment with them either through the console here or using a Python script. So,
we've nearly concluded our discussion of Python file i/o. Have a look at the
challenges below. See if you can experiment with the write+ access
mode and write some example code to understand how it works and then using
the access modes that we've discussed today see if you can create a file and
then replace data as specific positions in that file.
In our concluding unit we're going to have a walkthrough of a mini project - a
quiz program that brings together everything we've learned over the past
few units.

## Output from Console:

dee2018:~/workspace (master) $ python3
Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open("data.txt", "r+")
>>> f.write(lines)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lines' is not defined
>>> lines = f.read()
>>> print(lines)
Line 1
Line 2
Line 3

>>> f.write("Line 4\n")                                                                                      
7
>>> close()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'close' is not defined
>>> f.close()
>>> f = open("data.txt", "r+")
>>> f.write("foo")
3
>>> f.close()
>>> f = open("data.txt", "a+")
>>> f.tell()
22
>>> f.seek(0)
0
>>> f.write("Foo")
3
>>> f.close()
>>> 


