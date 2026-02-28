feet=int(input('Enter length in feet '))
while True:
    print('1. Inches')
    print('2. Yards')
    print('3. Miles')
    print('4. Millimeters')
    print('5. Centimeters')
    print('6. meters')
    print('7. Kilometers')
    print('8. Exit')
    sid=int(input('Enter your choice '))
    if sid==1:
        con=feet*12
    elif sid==2:
        con=feet/3.0
    elif sid==3:
        cov=feet/5280.0
    elif sid==4:
        con=feet*304.8
    elif sid==5:
        con=feet*30.48
    elif sid==6:
        con=feet*0.3048
    elif sid==7:
        con=feet*0.0003048
    elif sid==8:
        break
    print('The required result= ',res)
