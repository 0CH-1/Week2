#Adventure type
type_of_adventure=input("Which type of adventure should I have? ")
if type_of_adventure == "scary" or type_of_adventure == "short":
    print("Entering the dark forest!")
elif type_of_adventure == "safe" or type_of_adventure == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

#Parcel price
size=input("Which size is the parcel? ")
weight=input("What is the weight of the parcel? ")
if size == "large" and weight == "heavy":
    print("This parcel will be expensive to deliver")
else:
    print("This parcel will be expensive to deliver")

#Dark forest setting
hear=input("Wha did I hear?")
see=input("What did I see?")
if hear =="grr" and see =="two red eyes":
    print("There is a scary creature. I should get out of here")
else:
    print("I'm a little scared but I will continue")

