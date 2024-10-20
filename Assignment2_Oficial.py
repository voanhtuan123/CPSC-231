list_num = 0
while list_num < 2: #re-enter a datapoint if a datapoint is less than 2
    list_num = int(input("How many data points do you have? "))
    if list_num < 2:
        print("Must enter at least two data points.")

x = 1
years = []
fertility = []
while x <= list_num: #enter the year and the fertility value
        print("What is the year of Datapoint",x,"?" )
        year = int(input())
        print("What is the fertility rate of Datapoint",x,"?")
        fertility_rate = float(input())

        if year in years: #replace the value of fertility if user enter the same year 
            fertility_rate = years.index(year)
        else: #if the year is not duplicate, append the value into the list
            years.append(year)
            fertility.append(fertility_rate)
            x = x + 1
            
start_year = int(input("Which year you would like to start with?")) #enter start year 
if start_year in years: 
    end_year = int(input("Which year you would like to end with?"))#enter end year
    if end_year in years:
        if end_year > start_year: 
            ave = (fertility[years.index(start_year)] + fertility[years.index(end_year)])/2
            print(f"The average fertility rate of these two years is {ave:.2f}.") #export average fertilitty 
            if fertility[years.index(start_year)] > fertility[years.index(end_year)]: #export the trend of fertility
                print("There is a downward trend.")
            elif fertility[years.index(start_year)] < fertility[years.index(end_year)]:
                print("There is an upward trend.")
            else:
                print("There is a sideways trend.")
        else:
            print("End year must be after start year.") #end the code if end year greater than start year
    else:
        print("The end year does not exist.") #end the code if a end year has not entered
else:
    print("The start year does not exist.") #end the code if a start year has not entered