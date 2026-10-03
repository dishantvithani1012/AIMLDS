# write a program to findout whether given shape is portrait or landscape or square from user given length and width.
#task findout display ratio of width vs length

length = int(input(" enter the length"))
width = int(input(" enter the width"))

if length >width:
    print("Shape is portrait")
if width > length:
    print("Shape is landscape")
if length == width:
    print("Shape is Square")
print("Good bye")