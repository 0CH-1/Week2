type_of_adventure=input("Which type of adventure should I have? ")
if type_of_adventure == "scary" or type_of_adventure == "short":
    print("Entering the dark forest!")
elif type_of_adventure == "safe" or type_of_adventure == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
