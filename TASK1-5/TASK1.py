# 1-ci tapşırıq: 5-ə bölünüb-bölünmədiyini tapmaq

def main():
    try:
        num = int(input("Bir ədəd daxil edin: "))
        if num % 5 == 0:
            print(f"{num} → 5-ə bölünür ")
        else:
            print(f"{num} → 5-ə bölünmür ")
    except ValueError:
        print("Xahiş olunur yalnız tam ədəd daxil edin!")

if __name__ == "__main__":
    main()
