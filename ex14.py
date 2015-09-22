from sys import argv

script, username = argv
prompt = '> '

print "Hello %s, I am the %s script." % (username, script)
print "I'd like to ask you a few questions."

print "Do you like me, %s?" % username
likes = raw_input(prompt)

print "Where do you live %s?" % username
lives = raw_input(prompt)

print "%s, what type of computer do you have?" % username
computer = raw_input(prompt)

print """
Ok, so you said %r about liking me.
You said you live %r. Not sure where that is.
You also said you have a %r computer. Nice.
""" % (likes, lives, computer)
