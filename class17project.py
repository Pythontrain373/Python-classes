bill=int(input("What is the bill: "))
pay=int(input("How much did you pay: "))
if bill<pay:
    answer=pay-bill
    print("The shopkepper owes you",answer,"dollars")
elif bill==pay:
    print("The full bill if paid")
elif bill>pay:
    answer=bill-pay
    print("You owe the shopkepper",answer,"dollars")
else:
    print("Invalid answer")