print("Enter any two number: ");
num1 = input();
num2 = input();
try:
  add = int(num1) + int(num2);
  print(num1, "+", num2, "=", add);
  sub = int(num1) - int(num2);
  print(num1, "-", num2, "=", sub);
  mul = int(num1) * int(num2);
  print(num1, "*", num2, "=", mul);
  div = int(num1) / int(num2);
  print(num1, "/", num2, "=", div);
except ZeroDivisionError:
    print("You can't divide by zero!");


