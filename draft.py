Question1 = input("Are you a Canadian citizen? ")               #ask if the user is a Canadian citizen
if Question1 not in ["yes", "Yes", "no", "No"]:                 #end the code if user enter wrong command
        print("Invalid response")
        quit()

Question2 = input("Are you a resident of Alberta?")             #ask if the user is a residence of alberta
if Question2 not in ["yes", "Yes", "no", "No"]:              #end the code if user enter wrong command
        print("Invalid response.")
        quit()

Question3 = input("What is the month of your birth date?")       #ask for the month of birth date 
if Question3 not in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]: #end the code if user enter wrong command
        print("Invalid response.")
        quit()

Question4 = int(input("What is the day of your birth date?"))    #ask for the day of birth date
if Question4 not in range(1,32):              #end the code if user enter wrong command
        print("Invalid response.")
        quit()

Question5 = int(input("What is the year of your birth date?"))   #ask for the year of birth date
if Question5 not in range(1900,2025):                            #end the code if user enter wrong command
    print("Invalid response.")
    quit()

if Question1 == "Yes" or Question1 == "yes":        #check whether user is Canadian or not
    if Question2 == "Yes" or Question2 == "yes":        #check whether user is a Alberta residence or not
        if Question3 == "January" or Question3 == "February" or Question3 == "March" or Question3 == "April" or Question3 == "May" or Question3 == "June" or Question3 == "July" or Question3 == "August" or Question3 == "September" or Question3 == "October" or Question3 == "November" or Question3 == "December":  # Check the validity of birth date and whether user is 18 year old or not
            if Question5 < 2007:    #if users were born after 2007, they are not eligible
                if Question4 in range(1,32):
                    if Question4 in range (1,28):     #if user was born before 2006 and before day 28th but after October, they are not eligible
                        if Question3 == "October" or Question3 == "November" or Question3 == "December":
                            print("You are not eligible to vote.")
                        else:
                            print("You are eligible to vote.")
                    elif Question4 == 28:  #if user was born before 2006 and on day 28th but after September, they are not eligible
                        if Question3 == "September" or Question3 == "October" or Question3 == "November" or Question3 == "December":
                            print("You are not eligible to vote.")
                        else:
                            print("You are eligible to vote.")
                    elif Question4 == 29:
                        if Question5 % 4 != 0:
                            if Question3 == "February": 
                                print("Invalid birth date")
                            elif Question3 == "September" or Question3 == "October" or Question3 == "November" or Question3 == "December":
                                print("You are not eligible to vote.")
                            else: 
                                print("You are eligible to vote.")
                        else:
                            if Question3 == "September" or Question3 == "October" or Question3 == "November" or Question3 == "December":
                                print("You are not eligible to vote.")
                            else:
                                print("You are eligible to vote.")
                    elif Question4 == 30:    #if user was born before 2006 and on day 29th and 30th and before August, they are eligible excluding February
                        if Question3 == "February": 
                            print("Invalid birth date")
                        elif Question3 == "September" or Question3 == "October" or Question3 == "November" or Question3 == "December":
                            print("You are not eligible to vote.")
                        else: 
                            print("You are eligible to vote.")
                    else:   #if user was born before 2006 and on day 31st and in April and in June, they are eligible excluding September
                        if Question3 == "April" or Question3 == "June":
                            print("You are eligible to vote.")
                        elif Question3 == "September":
                            print("You are not eligible to vote.")
                        else: 
                            print("Invalid birth date")
            else: 
                print("You are not eligible to vote.")
    else :
        print("You are not eligible to vote.")
else:
    print("You are not eligible to vote.")