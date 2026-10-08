#Books message
genre=input("What type of book is is this? ")
print(f"I like "+ genre + " books!")
print ("Finished reading book.")

#number input comparison
first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
if first>second:
    print("The first number is bigger")
else:
    print("The first number is equal or smaller!")
print("Done!")

#Calculating activity
activity=input("Please enter an activity to be performed. ")
print(f"performing " + activity)
print("Activity completed!")

#Maze navigation
direction=input("Towards which direction should I go (up, down, left, or right)? ")
if direction=="up":
 print(f"I am moving in upward direction!")
elif direction=="down":
    print(f"I am moving in downward direction!")
elif direction=="left":
    print(f"I am moving in left direction!")
elif direction=="right":
    print(f"I am moving in right direction!")
else:
    print(f"I am lost")

#odd/even
num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

#smallest num
first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
if first>second:
    print("The second number is smallest")
else:
    print("The first number is smallest")

#odd/even counter
odd_number = 0
even_number = 0
first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
third=int(input("Enter the third number: "))
if first%2==0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if second%2==0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if third%2==0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
print(f"There were {even_number} even numbers and {odd_number} odd numbers.")


