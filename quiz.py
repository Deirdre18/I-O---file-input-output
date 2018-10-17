#We want to define a variable f and it will open our data txt file for reading. Then we're going to call the readlines() method and put that in the variable lines. We'll close our file handle and then we'll print the results to screen. When we save and run this, our output will be as follows. The code opened the file, read the lines into a variable called lines and as you can see, we have a list of strings. We can also see that each one contains a newline character, which is the \n and this makes sense because the file contains four separate lines. The readlines() method splits this at those newline characters to create a line of strings. 

#A very simple practical thing we can do with text files is to count the occurrences of words. The Project Gutenberg website provides books that are out of copyright in text format. For this example we'll use "The Secret Adversary", by Agatha Christie. So, open up the link below as we are doing here, and select some text. Take about a page of it. I'm going to copy that, and then we'll create a new file in our project, which we're going to call book.txt. Then we can paste our text into it. Save that and then create a new Python script called book.py.

#f = open('data.txt', 'r')
#lines = f.readlines()
#f.close()
#print(lines)


#If we modify it slightly and use the read() method instead of readlines(), then see how it changes. Now, all of the data is read into a single string including the newline characters it now appears just as text and not as a list of strings. The newline character causes the string to be displayed over the four lines of our file.

#Relative and Absolute Paths
#In this unit we're going to have a look at relative and absolute paths. This refers to how we find files and resources on our file system. As we remember from our last unit, the open() function opens a file and returns a file handle which we stored in f. The first argument of the open() function is the file name and, up until now, we've been using files that are in the same directory as the Python script we're running, so only the file name was needed. But, there's nothing to stop us from opening files in other directories too. So, let's do this. Let's create a subdirectory in our project called "files". There are a couple of ways of doing this. We can right-click on our project and then go down to New Folder at the bottom of the menu, or we can do it in our terminal window by typing mkdir and then "files" - the name of our directory. When we do this, we'll notice then that "files" appears in the left-hand pane of our Cloud9 window. So, let's create a new file in there - a text file. We're going to call it relative_data.txt. Then let's add some content to it. For lack ofFor lack of imagination, I'm just adding lines 1, 2, 3 & 4. We'll save that, and then we'll modify our quiz.py script to open it. 

#Then we'll modify our quiz.py script to open it. First we supply the name of the subdirectory which, in this case, is files and then /relative_data.txt. Let's save this and run it to check that it works. Here we can see that our content is returned from our relative_data.txt file just as it was before. This is what's known as a relative path it identifies the location of the data file relative to the script that's currently running. It starts in a given location - the working directory that we're in - and works down from there. By contrast an absolute path starts at the very top of the file system. An absolute path is not relative to the running program but rather it's a fully formed path to a specific file. We can demonstrate this by going to our terminal window and changing into the files directory that we created earlier. So let's do that now. We'll clear the screen first. Change into our files directory using CD, and now we're going to use the PWD command, which is short for Print Working Directory. We can see that this gives us our current location on the file system. We can also find the absolute path of an individual file using the readlink command here with the -f switch. We'll use it, and then find the absolute path to relative_data.txt. There we can see where it is on the file system. So, let's just try this. Let's take a copy of this, put it into our quiz.py files to open it and see if it works. We'll also just change back up to the previous directory that we were in so that we can run our script. We'll paste that in there, we'll clear the screen and we'll run our script just to see if it's working - and indeed it is. So, we can see that to open a file using an absolute or a relative path is very straightforward in Python. We just specify the path in the open command. We don't need to do anything else. Generally speaking, though, if you can refer to a file using a relative path then do so. Absolute paths couple applications very tightly to the file system. It's normally unnecessary to rely on a file being in a specific location like that. An exception might be where there's a dependency on a third-party file. For example, in our boggle project, Mac users could use the built-in dictionary that comes pre-installed on that machine. That's a scenario where using an absolute path makes sense because it avoids the need to distribute a dictionary with the app. But if you do use absolute paths, make sure that they're easily changeable. if Cloud9 moved this project to a different server or changed their file system, then trying to open our relative_data.txt file with an absolute path would no longer work. So, declare them as constants in your code or - even better - keep them in a separate configuration file in your project or in an environment variable. Now that we've seen how to open resources using absolute or relative paths, in our next unit we're going to look at how to write a file in Python



#f = open('data.txt', 'r')
#lines = f.readlines()
#f.close()
#print(lines)

f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')
lines = f.read()
f.close()
print(lines)




