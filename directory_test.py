import os
import re
#pattern = re.compile("^[789]\d{9}$")
pattern = re.compile("^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")

#To find the text which is equialent to phone numbers
def regmat(line1):
    list1 =line1.split("\n")
    for element in list1:
            if re.match(pattern, element) is not None:
                    print element
            
#Recursively traversing directories using oswalk
def directo(path):
     print "The phone numbers in the set of files are:"
     for dirpath, dirs, files in os.walk(path): #Path of directory 
          for filename in files:
              fpath = os.path.join(dirpath,filename)
              with open(fpath) as impfile:
                  line = impfile.read()
                  regmat(line)

                   
                 		    		
path = input("Give the path of the directory to be searched(starting with ./)")
directo(path)
   
