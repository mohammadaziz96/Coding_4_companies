#Question1: was just about numbers(changing every digit of a number to 9-digit value) for example: 253 should be changed to 746, 304 should be changed to 695 etc.

def ChangingDigits(num):
    result=""
    for i in str(num):
        result=result+str(9-int(i))
    return int(result)
n=int(input("Enter numbers: "))
print(ChangingDigits(n))
