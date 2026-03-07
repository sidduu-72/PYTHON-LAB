a=["inches", "yards", "miles", "millimetres", "centi meters","meters","kilo meters"]
b=[12,1/3,1/5280,304.8,30.48,0.3048,0.0003048]
n=int(input("Enter a numer:"))
k=int(input("Enter a value to read\n 1.inches\n 2.yards\n 3.miles\n 4.millimetres\n 5.centi meters\n 6.meters\n 7.kilo meters\n"))
while k<8:
    n=int(input("Enter a valid option:"))
    print(n,"Feet:",n*b[k-1],a[k-1])
    break;
   
