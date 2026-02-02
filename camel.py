def camel_case(): 

 string1 = input("input a string in camel case e.g youTube : ")
 string2 = ""

 for character in string1:
     if character.isupper():
         string2 = string2 + "_"+character.lower()
     else:
         string2 = string2 + character
 print(string2)

camel_case()