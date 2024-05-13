print("SELECT OPERATOR!")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

def Add(num1, num2):
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Mul(num1 , num2):
    return num1 * num2

def Divi(num1, num2):
    return num1 / num2

while True:
    opt_input = input("Choose the operation (1/2/3/4)  :")
    if opt_input in ("1","2","3","4"):
        first_num = float(input("Enter your first number = "))
        second_num = float(input("Enter your second number = "))
        if opt_input == "1":
            result = Add(first_num,second_num)
            print(f"{first_num} + {second_num} = {result}")
        elif opt_input == "2":
            result = Sub(first_num,second_num)
            print(f"{first_num} - {second_num} = {result}")
        elif opt_input == "3" :
            result = Mul(first_num,second_num)
            print(f"{first_num} x {second_num} = {result}")
        elif opt_input == "4" :
            result = Divi(first_num,second_num)
            print(f"{first_num} % {second_num} = {result}")

        next_time = input("Do you want to continue: (yes or no)").lower()
        if next_time == 'no':
            break
    else:
        print("Invalid Number!")



    
