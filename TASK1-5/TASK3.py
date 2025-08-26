# 3-cü tapşırıq: Sadə kalkulyator

def main():
    try:
        n1 = float(input("1-ci ədədi daxil edin: "))
        op = input("Əməliyyatı daxil edin (+, -, *, /): ").strip()
        n2 = float(input("2-ci ədədi daxil edin: "))

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            result = "Sıfıra bölmək olmaz!" if n2 == 0 else n1 / n2
        else:
            result = "Yanlış əməliyyat seçildi!"

        print("Nəticə:", result)
    except ValueError:
        print("Xahiş olunur yalnız ədəd daxil edin!")

if __name__ == "__main__":
    main()
