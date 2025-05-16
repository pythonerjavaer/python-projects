from person import Person

#####################
## Create a person ##
#####################
arthur = Person("Arthur")

#####################
## Adding children ##
#####################
arthur.add_child(Person("Bill"))
arthur.add_child(Person("Charlie"))
arthur.add_child(Person("Percy"))

# (We can add children like this too)
fred = Person("Fred")
arthur.add_child(fred)

george = Person("George")
arthur.add_child(george)

ron = Person("Ron")
arthur.add_child(ron)

ginny = Person("Ginny")
arthur.add_child(ginny)

#######################
## Count descendants ##
#######################
print(arthur.count_living_descendants())
# -> 7

######################
## List of children ##
######################
print(arthur.get_children_names())
# -> ['Bill', 'Charlie', 'Percy', 'Fred', 'George', 'Ron', 'Ginny']

##################
## People dying ##
##################
fred.dies()
# -> print "Fred has died :("

print(arthur.count_living_descendants())
# -> 6

#############################
## Adding more descendants ##
#############################
ron.add_child(Person("Rose"))
ron.add_child(Person("Hugo"))

ginny.add_child(Person("James"))
ginny.add_child(Person("Albus"))
ginny.add_child(Person("Lily"))

print(arthur.count_living_descendants())
# -> 11

print(ginny.count_living_descendants())
# -> 3