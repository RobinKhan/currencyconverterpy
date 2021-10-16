US_Dollar = 84.75
Euro = 101.42
British_Pound = 118.24
Australian_Dollar = 65.95
Canadian_Dollar = 67.36
Swiss_Franc = 91.55
Japanese_Yen = 0.78
Saudi_Arabian_Riyal = 22.60

ALL_CURRENCY = ['1. US Dollar', '2. Euro', '3. British_Pound', '4. Australian_Dollar', '5. Canadian_Dollar',
                '6. Swiss_Franc', '7. Japanese_Yen', '8. Saudi_Arabian_Riyal']

print("in new line")
print(*ALL_CURRENCY, sep="\n")

ameDollar = 85

valInput = input("Enter you from list 1-7 :- ")


def currecyconvert():
    if valInput == '1':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * US_Dollar)
        print('Total amount is = ' + str(res))
    elif valInput == '2':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * Euro)
        print('Total amount is = ' + str(res))
    elif valInput == '3':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * British_Pound)
        print('Total amount is = ' + str(res))
    elif valInput == '4':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * Australian_Dollar)
        print('Total amount is = ' + str(res))
    elif valInput == '5':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * Canadian_Dollar)
        print('Total amount is = ' + str(res))
    elif valInput == '6':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * Swiss_Franc)
        print('Total amount is = ' + str(res))
    elif valInput == '7':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * Japanese_Yen)
        print('Total amount is = ' + str(res))
    elif valInput == '8':
        amt = int(input("Enter BDT amount to convert :- "))
        res = (amt * Saudi_Arabian_Riyal)
        print('Total amount is = ' + str(res))
    else:
        print("Not valid input")


if __name__ == '__main__':
    currecyconvert()
