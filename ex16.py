from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3)

print ("And finally, we close it.")
target.close()

print ("And then we open it again to be able to read it.")
target = open(filename, 'r')

print ("And here are the contents of the file: ", target.read)

print ("And then we close it one more time.")
target.close()
