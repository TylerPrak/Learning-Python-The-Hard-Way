tabby_cat = "%sI\'m tabbed in." % '\t'
persian_cat = "I\'m split%son a line." % '\n'
backslash_cat = "I\'m \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print '%r' %backslash_cat
print fat_cat
