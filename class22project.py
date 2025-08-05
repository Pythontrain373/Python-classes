def multiply_tuple_numbers(numbers):
    result=1
    for number in numbers:
        result=result*number
    return result
my_tuple=(1,2,3,4,5)
product=multiply_tuple_numbers(my_tuple)
print(product)
