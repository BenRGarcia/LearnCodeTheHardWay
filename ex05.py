my_name = 'Rip van Winkle' # or is it?
my_age = 103 # totally a lie
my_height = 70 # inches
my_weight = 180 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eye and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s white depending on the coffee." % my_teeth

# this line is tricky, try to get it right!
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Python format characters are :"
print "%c", "character"
print "%s", "string"
print "%i", "signed decimal integer"
print "%d", "signed decimal integer"
print "%u", "unsigned decimal integer"
print "%o", "octal integer" # what the heck is that?!
print "okay, I get the point, I found the other format characters on 'the google'... you've made your point Zed :-P"