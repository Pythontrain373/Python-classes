"""Square it Out!
Outline:
Create a list of square values of numbers between specified ranges by the user, and then separate the odd and even values."""
#I serched how to do line 6 to 8 on google can you help me next lesson
def square(start,end):
    squares=[i**2 for i in range(start,end+1)]
    even_squares=[x for x in squares if x%2==0]
    odd_squares=[x for x in squares if x%2!=0]
    return even_squares,odd_squares
start=int(input("Enter the start of the range: "))
end=int(input("Enter the end of the range: "))
even_squares,odd_squares=square(start, end)
print("Even squares:",even_squares)
print("Odd squares:",odd_squares)