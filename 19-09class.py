string = input("Enter your string: ")
for i in string: 
    if i.isalnum:
        print("string contains alpha and numeric values")
        if i.isalpha:
           print("string contains alphabetical characters")
           if i.isupper:
               print("string is in uppercase")
           else:
              print("string is in lowercase")         
        else:
            print("string is an digit")    
    elif i.isspace:
      print("which is in empty")
    else:
       print("special characters")
print(string)          