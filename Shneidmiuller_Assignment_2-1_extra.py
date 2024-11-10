input_boys_string = str(input("Enter boys' names for list, separated by spaces: "))
input_girls_string = str(input("Enter girls' names for list, separated by spaces: "))
boys_list = input_boys_string.split()  
girls_list = input_girls_string.split()  

boys_sorted = sorted(boys_list)
girls_sorted = sorted(girls_list)

if len(boys_list) != len(girls_list):
    print ("Can't match :(")
else:
    print("Lists before sorting:", boys_list, girls_list)
    print("Lists after sorting:", boys_sorted, boys_sorted)
    for boys_list, girls_list in zip(boys_sorted, girls_sorted):
        print(f"{boys_list} and {girls_list}")
