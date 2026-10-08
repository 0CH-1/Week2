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