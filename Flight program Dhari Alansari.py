while True:
    print("\n1. See available flights")
    print("2. Book a flight")
    print("3. Exit")

    menuchoice = float(input("Choose one of the above: "))

    if menuchoice > 3 or menuchoice < 1:
        print("\nInvalid choice, please choose a number between 1 and 3.")
        continue  # This will restart the loop, prompting the user again.

    if menuchoice == 1:
        print("\nThese are the available flights right now.")
        print("1. New York")
        print("2. London")
        print("3. Kuwait")
        print("4. Tokyo")
        citychoice = float(input("Pick a city to get information about the flight: "))

        if citychoice > 4 or citychoice < 1:
            print("Invalid choice, please choose a number between 1 and 4.")
            continue  # Restart the loop

        # Gives different information depending on the choice that the user makes
        if citychoice == 1:
            print("\nDestination: New York")
            print("Flight number: NY208")
            print("Airline name: British Airways")
            print("Aircraft number: BA105")
            print("Origin: Paris")

        elif citychoice == 2:
            print("\nDestination: London")
            print("Flight number: LHR341")
            print("Airline name: Kuwait Airways")
            print("Aircraft number: KU765")
            print("Origin: Kuwait City")

        elif citychoice == 3:
            print("\nDestination: Kuwait")
            print("Flight number: KU243")
            print("Airline name: Kuwait Airways")
            print("Aircraft number: KW998")
            print("Origin: Amsterdam")

        elif citychoice == 4:
            print("\nDestination: Tokyo")
            print("Flight number: EK628")
            print("Airline name: Emirates Airways")
            print("Aircraft number: EK234")
            print("Origin: Dubai")

    elif menuchoice == 2:
        print("Option 2 selected - Book a flight")
       #asks user to choose a flight
        print("\nWhich flight would you like to book?")
        print("1.New York")
        print("2.London")
        print("3.Kuwait")
        print("4.Tokyo")
        #variable for the input
        bookflight = float(input("Pick a flight you would like to book: "))
        
        if bookflight > 4 or bookflight < 1:
            print("\ninvalid choice, please choose a number from the list")
            continue #This will restart the loop for the booking section.
    
        else:
          confirmbooking =  float(input("\nType 1 to confirm your booking: "))
          
          if confirmbooking != 1:
              print("booking canceled.")
    
          else:
              print("Flight booked successfully!")
              break #once the user confirms the booking, the loop stops and the program ends.
    
    
    elif menuchoice == 3:
        print("Exiting program. Goodbye!")
        break  # Exit the loop and end the program
