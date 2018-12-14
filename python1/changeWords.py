import sys
path = sys.argv[1]
textfile = open(path, 'r')
string = textfile.read()
print(string)
textfile.close
string = string.replace(" i ", " oraz ")
string = string.replace(" oraz ", " i ")
string = string.replace(" nigdy ", " prawie nigdy ")
string = string.replace(" dlaczego ", " czemu ")
print(string)

