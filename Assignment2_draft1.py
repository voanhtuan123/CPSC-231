list_num = 0
while list_num < 2:
    list_num = int(input("How many data points do you have? "))
    if list_num < 2:
        print("Must enter at least two data points.")

x = 0
years = []
fertility = []
while x < list_num: 
        x = x + 1
        print("What is the year of Datapoint",x,"?" )
        years.append(int(input()))
        print("What is the fertility rate of Datapoint",x,"?")
        fertility.append(float(input()))
print(years)
print(fertility)
            
start_year = int(input("Which year you would like to start with?"))
if start_year in years:
    end_year = int(input("Which year you would like to end with?"))
    if end_year in years:
        if end_year > start_year:
            ave=(fertility[years.index(start_year)] + fertility[years.index(end_year)])/2   
            print("The average fertility rate of these two years is", round(ave,2))
            if fertility[years.index(start_year)] > fertility[years.index(end_year)]:
                print("There is a downward trend.")
            elif fertility[years.index(start_year)] < fertility[years.index(end_year)]:
                print("There is a upward trend.")
            else:
                print("There is a sideways trend.")
        else:
            print("End year must be after start year.")
    else:
        print("The end year does not exist.")
else:
    print("The start year does not exist.")