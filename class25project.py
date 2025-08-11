try:
    user_input=int(input("Enter a number: "))
    if user_input<=0:
        print("Please enter a positive number.")
    else:
        odd_numbers_list_1=[i for i in range(1, user_input) if i%2!=0]
        odd_numbers_list_2=odd_numbers_list_1.copy()
        print("First list of odd numbers: ", odd_numbers_list_1)
        print("Second list of odd numbers: ", odd_numbers_list_2)
except ValueError:
    print("Invalid input.Please enter an number.")
fruits_list=["apple", "banana", "cherry", "dates"]
capitalized_fruits_list=[fruit.capitalize() for fruit in fruits_list]
print("Original fruits list: ",fruits_list)
print("Capitalized fruits list: ",capitalized_fruits_list)

#line 6,7 and 13 were copied form google pls explane next class