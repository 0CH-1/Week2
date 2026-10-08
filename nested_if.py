#book cover
cover_type=input("what type of cover does the book have? (hard/soft) ")
if cover_type== "soft":
    bound=input("Is the book perfect-bound? ")
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")

#phone location
where_to_look=input("Where to look at? ")
if where_to_look == "in the bedroom":
    bedroom=input("Where in the bedroom should I look?")
    if bedroom =="Under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")

elif where_to_look == "in the bathroom":
    bathroom=input("Where in the bathroom should I look?")
    if bathroom =="in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")

elif where_to_look == "in the living room":
     living_room=input("Where in the living room should I look?")
     if living_room =="on the table":
         print("Yes I found my phone!")
     else:
         print("Found some stuff but no phone")

else:
    print("I don't know where that is but I will keep looking")