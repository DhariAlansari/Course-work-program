while True:
    # Display the main menu options
    print("\n1. See available flights")
    print("2. Book a flight")
    print("3. Exit")

    # Get the user's choice
    menuchoice = float(input("Choose one of the above: "))

    # Validate the user's choice
    if menuchoice > 3 or menuchoice < 1:
        print("\nInvalid choice, please choose a number between 1 and 3.")
        continue  # Restart the loop if the choice is invalid

    if menuchoice == 1:
        # Display available flights for different cities
        print("\nThese are the available flights right now.")
        print("1. New York")
        print("2. London")
        print("3. Kuwait")
        print("4. Tokyo")
        # Get the user's choice for a specific city
        citychoice = float(input("Pick a city to get information about the flight: "))

        # Validate the user's city choice
        if citychoice > 4 or citychoice < 1:
            print("Invalid choice, please choose a number between 1 and 4.")
            continue  # Restart the loop if the choice is invalid

        # Provide information about the selected flight
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
        # Display available flights for booking
        print("\nWhich flight would you like to book?")
        print("1. New York")
        print("2. London")
        print("3. Kuwait")
        print("4. Tokyo")
        # Get the user's choice for booking
        bookflight = float(input("Pick a flight you would like to book: "))

        # Validate the user's booking choice
        if bookflight > 4 or bookflight < 1:
            print("\nInvalid choice, please choose a number from the list")
            continue  # Restart the loop for the booking section

        else:
            # Confirm the booking with the user
            confirmbooking = float(input("\nType 1 to confirm your booking: "))

            if confirmbooking != 1:
                print("Booking canceled.")
            else:
                print("Flight booked successfully!")
                break  # End the program after successful booking

    elif menuchoice == 3:
        print("Exiting program. Goodbye!")
        break  # Exit the loop and end the program
