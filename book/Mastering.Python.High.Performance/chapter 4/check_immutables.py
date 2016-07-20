

a = "This is a string"
b = "This is a string"

print id(a) == id(b)  #prints  True

print id(a) == id("This is a string") #prints True

print id(b) == id("This is another String") #prints False