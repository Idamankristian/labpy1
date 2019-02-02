a = int(input ("masukan nilai a : "))
b = int(input ("masukan nilai b : "))
c = int(input ("masukan nilai c : "))

if a > b :
    if a > c :
        print ("nilai terbesarnya adalah", a)
    else :
        print ("nilai terbesarnya adalah", c)
elif b > c :
    print ("nilai terbernya adalah", b)
else :
    print ("nilai terbesernya adalah", c)
