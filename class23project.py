def check_frequency(test_dict, value):
    return list(test_dict.values()).count(value)
my_dict = {'a':1,'b':2,'c':1,'d':3}
value = 1
frequency = check_frequency(my_dict, value)
print("The frequency of",value,"is:",frequency)