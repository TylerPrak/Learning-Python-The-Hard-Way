#STUDYDRILLS
# Find all places where a string is put inside a string. There are four places.
#
# Explain why adding the two strings 'w' and 'e' with '+' makes a longer string.
#	-Adding the two strings together with the addition operator(+) concatenates the two variables.


#Create and initialize variables

#'x' is a variable that contains a string and uses the integer(%d) format character
x = "There are %d types of people." % 10

#'binary' is a variable that contains a string
binary = "binary"

#'do_not' is a variable that contains a string
do_not = "don't"

#'y' is a variable that contains a string and uses the string(%s) format character
#Contains strings put inside another string. 2/4
y = "Those who know %s and those who %s." % (binary, do_not)

#Prints out the 'x' variable
print x

#Prints out the 'y' variable
print y

#Prints out a string and uses the raw(%r) format character 
#Contains a string put inside another string. 3/4
print "I said: %r." % x

#Prints out a string and uses the string(%s) format character
#Contains a string put inside another string. 4/4
print "I also said: '%s'." % y

#Create and initialized a variable called 'hilarious' containing the false boolean value
hilarious = False

#Create and initialized a variable called 'joke_evaluation' that has the raw(%r) format character and no following variable. Because of this, whenever we use this variable, we need to have a following '%' and variable.
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints out the variable 'joke_evaluation' with input from the variable 'hilarious'
print joke_evaluation % hilarious

#Create and initialized 2 string variables
w = "This is the left side of..."
e = "a string with a right side."

#Prints out the 'w' and then 'e' variable
print w + e
