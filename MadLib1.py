# Variable

print ("Enter a type of animal")
animal = raw_input()
if animal == "":
    animal = "squirrel"

print ("Enter a direction")
direction = raw_input()
if direction == "":
    direction = "around"

print ("Enter an object")
object = raw_input()
if object == "":
    object = "tree"

print ("Enter a type of precipitation")
example = raw_input()
if example == "":
    example = "snow"

print ("Enter action")
action = raw_input()
if action == "":
    action = "trapped"

print ("Enter a place")
place = raw_input()
if place == "":
    place = "inside"

print ("Enter an action that relates to the example")
action2 = raw_input()
if action2 == "":
    action2 = "melted"


# poem
print("The itsy bitsy " + animal + " climbed " + direction + " the " + object + ".")
print("Down came the " + example)
print("and " + action + " the " + animal + place + ".")
print("Out came the sun")
print("and " + action2 + " all the " + example)
print("and the itsy bitsy " + animal + " climbed " + direction + " the " + object + " again" + ".")
