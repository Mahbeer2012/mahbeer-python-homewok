valid = False 
while not valid: #using while loop
  try:
    n=int(int("enter a number:"))
    #enter a even number
    while n%2==0:  

     print("bye")
    valid = True
  except ValueError:
    print("Invalid")
