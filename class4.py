"""Average
Outline:
There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a 
sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?


tree1=int(input("Enter the hight of tree 1:"))
tree2=int(input("Enter the hight of tree 2:"))
tree3=int(input("Enter the hight of tree 3:"))
tree4=int(input("Enter the hight of tree 4:"))
tree5=int(input("Enter the hight of tree 5:"))
sum=tree1+tree2+tree3+tree4+tree5
answer=sum/5
print("The avarge of all the trees is",answer)



Count the notes
Outline:
Write a program to calculate the number of notes in the given amount?


amount=int(input("Please enter the amount\nPlease only write the number: "))
print("10 dollar note\n50 dollar note\n100 dollar note\n500 dollar note")
convort=int(input("Choose one of the notes above that you want to conver your amount into\nPlease only write the number: "))
finalsum=amount//convort
print("You will need",finalsum,convort,"dollar notes.To get enough notes for that",amount,"dollars")



Percentage calculation
Outline:
Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?


maths=int(input("What is the math marks: " ))
Science=int(input("What is the science marks: " ))
Hindi=int(input("what is the hindi marks: "))
ENglish=int(input("what is the english marks: "))
sum=maths+Science+Hindi+ENglish
answer=(sum/400)*100
print("Your percentage is",answer)"""