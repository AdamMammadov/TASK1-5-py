# 5-ci tapşırıq: Ədədin faktorialını tapmaq

def main():
    try:
        n = int(input("Ədəd daxil edin: "))
        if n < 0:
            print("Mənfi ədədin faktorialı yoxdur!")
            return
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        print(f"{n}! = {fact}")
    except ValueError:
        print("Xahiş olunur yalnız tam ədəd daxil edin!")

if __name__ == "__main__":
    main()
