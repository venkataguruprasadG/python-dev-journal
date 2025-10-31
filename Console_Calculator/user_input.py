import main_logic

while True:
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select your choice of arithmetic operation")

    if choice in ('1','2','3','4'):
        try:
            num1 = input("Enter the first number")
            num1_float = float(num1)

            num2 = input("Enter the second number")
            num2_float = float(num2)
        except ValueError:
            print("Invalid Input Please enter values only.")
            continue

        if choice == "1":
            print(main_logic.add(num1_float,num2_float))
        elif choice == "2":
            print(main_logic.sub(num1_float,num2_float))
        elif choice == "3":
            print(main_logic.mul(num1_float,num2_float))
        elif choice == "4":
            if num2_float == 0:
                print("Zero cannot be used for division.")
                continue
            print(main_logic.div(num1_float,num2_float))
        
        next_calculation = input("Do you want to perform another calculation ?(Yes/no)").lower()
        if next_calculation != "yes":
            break
    else:
        print("Invalid choice. Please enter a valid choice. (1,2,3,4)")    
        