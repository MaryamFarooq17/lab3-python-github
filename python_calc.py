print("-----------Menu-------------")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n" \
"5.Check Even or odd\n6.Calculate percentage\n7.Exit")

choice = int(input("Enter choice: "))

def check_even_odd(a,b):
    if a % 2 ==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
    if b % 2 ==0:
        print(f"{b} is even")
    else:
        print(f"{b} is odd")
    
while choice !=7:
    if choice < 1 or choice > 6:
        print("Invalid choice. Please select from 1 to 7.")
    else:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))

        if choice == 1:
            print("Process: Addition")
            Total = a+b
            print(f"Sum of {a} and {b} is: {Total}")
            
        elif choice == 2:
            print("Process: Subtraction")
            sub = a-b
            print(f"Subtraction of {a} and {b} is: {sub}")

        elif choice == 3:
            print("Process: Multiplication")
            product = a*b
            print(f"Product of {a} and {b} is: {product}")

        elif choice == 4:
            print("Process: Division")
            if b == 0:
                print("Denominator cannot be 0")

            else:
                div = a/b
                print(f"Divsion of {a} and {b} is: {div}")

        elif choice == 5:
            print("Process:Even/Odd check")
            check_even_odd(a,b)

        elif choice == 6:
            print("Process: Calculate Percentage")
            answer = input("Do you want to calculate number 1 as percentage of number 2: ")
            if answer in ("Yes", "yes"):
                if b==0: #denominator 0 check
                    print("Denominator cannot be 0")
                    
                else:
                    result = (a/b) * 100
                    print("Percentage: ", result)

            elif answer in ("No", "no"):
                print("Number 2 as percentage of number 1")
                if a == 0: #denomintor 0 check
                    print("Denominator cannot be 0")
                    
                else:
                    result = (b/a) * 100 
                    print("Percentage of number 2 to number 1:" , result)
            else:
                print("Invalid answer. Please enter Yes or No")
    print("-----------Menu-------------")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n" \
    "5.Check Even or odd\n6.Calculate percentage\n7.Exit")
    choice = int(input("Enter choice: "))

print("Exiting calculator. Goodbye!")