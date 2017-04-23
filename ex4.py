#STUDYDRILLS
#Traceback (most recent call last):
#	File "ex4.py", line 8, in <module>
#		average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
#
# Explain this error in your own words. Make sure you use line numbers
# and explain why.
#	-This error only shows because 'car_pool_capacity' is a variable that
#	 doesn't exist.
#
# I used 4.0 for 'space_in_a_car', but is that necessary? What happens if 
# it's just 4?
# 	-Using 4.0 isn't necessary unless we're dealing with values that 
#	 require floating point values. If the value was just 4 then the
#	 output for carpool_capacity would be 120 instead of 120.0.


#Create and initialize variables
cars = 100 
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
