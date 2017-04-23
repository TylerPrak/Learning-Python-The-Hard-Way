#Creates and initializes a variable called 'formatter' that has a string containg 4 raw(%r) format characters. This means that when we call this variable, it has to be followed by '%' and 4 variables wrapped inside parentheses and seperated by commas.
formatter = "%r %r %r %r"

#Prints out the variable 'formatter' followed by integer values.
print formatter % (1, 2, 3, 4)

#Prints out the variable 'formatter' followed by strings.
print formatter % ("one", "two", "three", "four")

#Prints out the variable 'formatter' followed by boolean values.
print formatter % (True, False, False, True)

#Prints out the variable 'formatter' followed by the same variable. This is gonna print out the 'formatter' string as it is, 4 times. 
print formatter % (formatter, formatter, formatter, formatter)

#Prints out the variable 'formatter' followed by strings. Due to the raw(%r) formatting character nature, it will print out the strings sometimes in single or double quotes.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
