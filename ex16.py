#Reading and Writing Files
from sys import argv

script, filename = argv

print "We are now going to erase %r." % filename
print "If you DO NOT want to proceed, click CTRL-C (^C)."
print "If you DO want to proceed, click RETURN or ENTER."

raw_input("?")

print "Opening up file..."
target = open(filename, 'w')

print "Truncating the file..."
print "Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Writing these into file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing file..."
target.close()
