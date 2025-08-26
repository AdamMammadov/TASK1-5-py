# 4-cü tapşırıq: 1-dən N-ə qədər ədədlərin cəmini tapmaq

def main():
    try:
        N = int(input("N daxil edin: "))
        if N < 1:
            print("N müsbət olmalıdır!")
            return
        cem = N * (N + 1) // 2   # daha sürətli formula
        print(f"1-dən {N}-ə qədər cəm:", cem)
    except ValueError:
        print("Xahiş olunur yalnız tam ədəd daxil edin!")

if __name__ == "__main__":
    main()
