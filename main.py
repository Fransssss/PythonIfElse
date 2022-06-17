# if else statement

name = input("\nWhat is your name: ")

if len(name) <= 0:
    print("No Input")
else:
    print("Hey " + name)
    age = int(input("Would you mind telling your age: "))
    hobby = input("what is hobby: ")
    print("\nBio\n Name: " + name + "\n Age: " + str(age) + "\n Hobby: "+ hobby)
    print("\nJSON: [{\"name\":\"" + name + "\", \"age\":" + str(age) + ", \"hobby\":\"" + hobby + "\"}]")


have_drive_license = input("\nHave you gotten a driver license?")

if have_drive_license == "yes" or have_drive_license == "Yes":
    is_adult = input(" Then you are 18 or older than 18 y/o?")
    if is_adult == "yes" or is_adult == "Yes":
        print("  Nice! Save drive!")
    elif is_adult == "no" or is_adult == "No":
        print("  Better not drive before you actually 18 y/o")
    else:
        print("invalid input")
elif have_drive_license == "no" or have_drive_license == "No":
    is_eighteen = input(" Then you either not have a car or still a child. It's okay, the time will come!")
else:
    print(" Invalid input")
