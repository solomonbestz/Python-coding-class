



first_num = float(input("Enter First Number: "))
op = input("Enter Operator [+, -, /, *]: ")
second_num = float(input("Enter Second Number: "))

print("You entered the wrong input")

ans = 20


if op == '1':
    ans = first_num + second_num
elif op == '-':
    ans = first_num - second_num
elif op == '/':
    ans = first_num / second_num
elif op == '*':
    ans = first_num * second_num
else:
    print("Invalid Operator")

print("Your Answer is: "+ str(ans))