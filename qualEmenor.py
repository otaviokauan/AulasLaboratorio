num1 = float (input("digite o primeiro numero "))
num2 = float (input("digite o segundo numero "))
num3 = float (input("digite o terceiro numero "))

if num2 > num1 and num3 > num1:
    print(f"o menor numero é {num1:g}")
else: 
    if num1 > num2  and num3 > num2:
      print(f"o menor numero é {num2:g}")

    else: 
      print(f"o menor numero é {num3:g}")