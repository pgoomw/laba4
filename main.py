def z1(a):
    if a%3 == 0:
        print("Делится")
    else:
        print("Не делится")
def z2(a):
    try:
        result = 100 / int(a)
        return result
    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError:
        print("Ошибка: нельзя делить на ноль")
    b = input()
    print(b)

def z3():
    try:
        day,month,year = input("Введите дату в формате XX.XX.XXXX: ").split(".")

        day = int(day)
        year = int(year)
        month = int(month)
        if day*month == year%100 :
            return True
        else:
            return False
    except ValueError:
        print("Введите дату в правильном формате")

def z4():
        ticket = input()

        first = ticket[:len(ticket)//2]
        second = ticket[len(ticket)//2:]
        s1,s2 = 0, 0
        for i in first:
            s1 += int(i)
        for j in second:
            s2 += int(j)
        if s1 == s2 :
            print("Счастливый")
            return True
        else:
            print("Несчастливый")
            return False





