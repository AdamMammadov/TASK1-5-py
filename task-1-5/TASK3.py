# 3-cü Task: Sadə kalkulyator
n1 = float(input("3-cü task: 1-ci ədədi daxil edin: "))
op = input("Əməliyyatı daxil edin (+, -, *, /): ")
n2 = float(input("3-cü task: 2-ci ədədi daxil edin: "))

if op == "+":
    print("Nəticə:", n1 + n2)
elif op == "-":
    print("Nəticə:", n1 - n2)
elif op == "*":
    print("Nəticə:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Nəticə:", n1 / n2)
    else:
        print("Sıfıra bölmək olmaz!")
else:
    print("Yanlış əməliyyat daxil etdiniz!")

print("-" * 40)