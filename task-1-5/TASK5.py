# 5-ci Task: Faktorial hesabla
factNum = int(input("5-ci task: Ədəd daxil edin: "))

if factNum < 0:
    print("Mənfi ədədin faktorialı yoxdur!")
else:
    fact = 1
    for i in range(1, factNum + 1):
        fact *= i
    print(f"{factNum}! =", fact)