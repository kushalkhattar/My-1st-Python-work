Balance = int(input("What is your current balance"))
B= int(input("What Amount you want to withdrow"))
if B < Balance:
    print("Withdrawal amount is valid. ")
    print("Your new balance is: ", Balance - B)
else:
    print("Invalid withdrawal amount.")
