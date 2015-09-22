a = "There are %d types of people." % 2
sports = "sports"
do_not = "don't"
b = "Those who play %s and those who %s." % (sports, do_not)

print a
print b

print "I said: %r." % a
print "I also said: '%s'." % b

funny = True
evaluation = "Isn't that funny?! %r"

print evaluation % funny
