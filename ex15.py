from sys import argv #from the sys library, import the argv module

script, filename = argv # ask for argument from command line

txt = open(filename) # declare a variable 'txt', open file

print ("Here's your file %r:" % filename) # print file name
print (txt.read()) # print .txt file contents
txt.close()

print ("Type your filename again:")
file_again = input("> ") # 2nd way to take user input, output .txt

txt_again = open(file_again)

print (txt_again.read())
txt_again.close()
