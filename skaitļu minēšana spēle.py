import random

slepenais_skaitlis = random.randint(1, 20)

print("Uzmini skaitli no 1 līdz 20!")

while True:
    minejums = int(input("Ievadi savu minējumu: "))

    if minejums > slepenais_skaitlis:
        print("Mēģini mazāku!")
    elif minejums < slepenais_skaitlis:
        print("Mēģini lielāku!")
    else:
        print("Apsveicu! Tu uzminēji!")
        break
    