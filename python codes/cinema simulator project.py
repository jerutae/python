film={
    "Tarzan":[15,5],
    "Finding nemo":[3,5],
    "Joker":[12,5],
    "Tangled":[18,5]}

while True:
    choice= input("What movie would you like to watch?:").strip().title()
    if choice in film:
        age=int(input("How old are you?:").strip())
        if age>= film[choice][0]:
            num_seats=film[choice][1]
            if num_seats>0:
                print ("Enjoy the film")
                film[choice][1]=film[choice][1]-1
            else:
                print("Sorry we are sold out!")
        else:
            print("You are too young for this!")
    else:
        print("We don't have that movie here")
