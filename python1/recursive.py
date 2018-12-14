import os
def listFiles(directory):
   for files in os.listdir(directory):
       path = os.path.join(directory, files);
       print (path)
       if os.path.isdir(path):
           listFiles(path)
directory = input("Podaj sciezke folderu: ")
listFiles(directory)
