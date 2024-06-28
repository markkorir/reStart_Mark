def categorize_age (age):
    if age < 0:
        return "Invalid Age"
    elif age <= 9:
        return "Generation Alpha"
    elif age <=24:
        return "Generation Z"
    elif age <=38:
        return "Millenials"
    elif age <= 73:
        return "Baby Bommers"
    else:
        return "silent Generation"
   
def main():
    try:
        age = int(input("Enter Your Age:"))
        generation = categorize_age (age)
        print (f"You belong to: {generation}")
    except ValueError:
        print ("Please Put a Valid Age")
 
if __name__ == "__main__":  
    main()            