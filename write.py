#In this unit, we're going to look at how to write to a file in Python. So, let's go ahead and create a new Python script in our project here. We'll call it write.py. Let's open that up and add some code to it. So, again, we use f as our file handle. We're going to use the open function and give it a file name, but this time we're going to use the 'w' argument for write, instead of the 'r' argument for read that we did before. Now, instead of read we're going to use write to write something to the file, and then we'll close it again. So, just thinking about that for a minute, looking at our access modes here - we're going to discuss those in a little bit more detail later - but you could have also put 'a' for append there. We'll have a look at that soon, but right now let's just run our file and see what happens. 


#f = open('newfile.txt', 'w')
#f.write ('Hello')
#f.close()

#So, first of all, as we can see over on the left hand pane here a new file has being created. And, if we open that up and have a look at the contents, you can see that it says Hello, which is exactly the content that we wanted to write to it from our script here. 

#But, what if we change the content that we're writing here? Let's change that to 'World'. We'll save it, we'll run it again, and now when we open our file first of all Cloud9 is going to tell us it's changed and asks if we want to reload it. So we will. Now it says World. 

#f = open('newfile.txt', 'w')
#f.write ('World')
#f.close()

#Notice what's happened here that the contents of the file have been overwritten! The content hasn't been appended to the end. If we want the content to be appended to the end of the file, then we need to change our file access mode here from write to 'a' for append. Let's do that. We'll change our content back to 'Hello', save it. We're just going to run the file a few times, and we'll see what happens. So, now, when we go into our newfile.txt file and have a look, we can see that everything has been appended. 'Hello' has been appended three times to the end of our file, but notice here that we don't have any new lines! It's all run together as one script. If we want, we can include newline characters if we want line breaks, and to do that we would just put \n which is the newline character. We'll delete our file, and then we'll run our script again just to demonstrate that this works. As you can see, whenever we delete it and then run the script again the file is recreated. We'll run it four times now and have a look at the contents again. So you have to reload, and now we can see that the text is nicely presented with newline characters. Each run of the program appends and writes to a new line. 

#f = open('newfile.txt', 'a')
#f.write ("Hello\n")
#f.close()

# Now, remember before we used the readlines method. We can also use the writelines method if we want to actually write a list of strings. So, let's create a variable called lines and in this we'll have our list. So, we're going to put 'Hello World, welcome to File I/O'. Okay, and then we're going to change the function here to writelines. We're going to use that method, and we'll change the content that we're writing here to lines instead of actual text. So, again we're going to delete our newfile.txt file. We'll save it, and let's just clear the screen here, and then run our script again. So, now a new file has been recreated.

f = open('newfile.txt', 'a')
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()

# What do we have this time? Well, again, it's now written a string but we have no new line characters, but as you can see the list that we gave has now been written. If we did want to add newline characters in, then we could do that. We could put the newline character at the end of each element here in our list, but the best way to do it is to actually use the join method. So, that's going to join this into one single string using \n as a separator. Now, instead we send text instead of lines to our file. So, let's delete it and let's run our script again. And, this time when we open it up and ask Cloud9 to reload it for us, then we can see that we have everything on nice neat new lines. So, that's how to write a file in Python. Our next unit will look at file access modes.