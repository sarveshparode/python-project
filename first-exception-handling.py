try:
    a=int(input("enter the value of numarator"))
    b=int(input("enter the value of denominator"))
    div=a//b
    print(div)
except ZeroDivisionError:
    print("zero is not denom")
except ValueError:
    print("enter only digit")
