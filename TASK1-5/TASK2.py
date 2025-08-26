# 2-ci tapşırıq: 3 ədədin ən böyüyünü tapmaqp

def main():
    try:
        nums = []
        for i in range(1, 4):
            n = int(input(f"{i}-ci ədədi daxil edin: "))
            nums.append(n)
        print("Ən böyük ədəd:", max(nums))
    except ValueError:
        print("Xahiş olunur yalnız tam ədəd daxil edin!")

if __name__ == "__main__":
    main()
