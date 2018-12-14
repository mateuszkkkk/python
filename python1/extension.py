import os
filename = input("Type file path with extension: ")
base = os.path.splitext(filename)[0]
os.rename(filename, base + ".png")
