"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
fp = open("foo.txt")

for line in fp:
    print(line)

fp.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print()
print()
bar = open("bar.txt", "r+")

# bar.write("The best thing about a boolean is even if you are wrong, you are only off by a bit.\nThe best method for accelerating a computer is the one that boosts it by 9.8 m/s2.\nIt’s not a bug – it’s an undocumented feature.\nOne man’s crappy software is another man’s full-time job.\nDon’t worry if it doesn’t work right. If everything did, you’d be out of a job.")

print(bar.read())

bar.close()
