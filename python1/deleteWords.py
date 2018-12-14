import sys
path = sys.argv[1]
textfile = open(path, 'r')
string = textfile.read()
print(string)
textfile.close
string = string.replace(" się ", " ")
string = string.replace(" i ", " ")
string = string.replace(" oraz ", " ")
string = string.replace(" nigdy ", " ")
string = string.replace(" dlaczego ", " ")
print(string)

